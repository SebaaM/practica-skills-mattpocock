from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TransactionTestCase

from .support import NOW


class RegistrationHistoryMigrationTests(TransactionTestCase):
    def test_existing_cancellations_keep_their_original_dates(self):
        before = [("activities", "0003_activity_responsible")]
        executor = MigrationExecutor(connection)
        after = executor.loader.graph.leaf_nodes()
        self.addCleanup(lambda: MigrationExecutor(connection).migrate(after))
        executor.migrate(before)
        old_apps = executor.loader.project_state(before).apps
        user = old_apps.get_model("auth", "User")
        teacher = user.objects.create(username="docente-migracion", is_staff=True)
        ana = user.objects.create(username="ana-migracion")
        bruno = user.objects.create(username="bruno-migracion")
        activity = old_apps.get_model("activities", "Activity").objects.create(
            title="Práctica", starts_at=NOW + timedelta(days=2), capacity=2, responsible=teacher,
        )
        registrations = old_apps.get_model("activities", "Registration").objects
        cancelled = registrations.create(activity=activity, student=ana, cancelled_at=NOW)
        registrations.create(activity=activity, student=bruno)

        executor = MigrationExecutor(connection)
        executor.migrate(after)
        apps = executor.loader.project_state(after).apps
        history = apps.get_model("activities", "RegistrationEvent").objects
        self.assertEqual(list(history.values_list("registration_id", "kind", "occurred_at")), [
            (cancelled.pk, "cancelled", NOW),
        ])

        self.client.force_login(get_user_model().objects.get(pk=teacher.pk))
        response = self.client.get(f"/teacher/activities/{activity.pk}/")
        self.assertContains(response, "<li>Cancelación · 01/10/2030 09:00</li>", html=True)
