# Generated by Django 1.10.5 on 2017-01-13 07:24

from django.db import migrations


class Migration(migrations.Migration):

    INDEX_SQL = """
CREATE INDEX msgs_msg_responded_to_not_null
ON msgs_msg (response_to_id)
WHERE response_to_id IS NOT NULL;

CREATE INDEX msgs_msg_visibility_type_created_id_where_inbound
ON msgs_msg(org_id, visibility, msg_type, created_on DESC, id DESC)
WHERE direction = 'I';

CREATE INDEX msgs_msg_org_modified_id_where_inbound
ON msgs_msg (org_id, modified_on DESC, id DESC)
WHERE direction = 'I';

CREATE INDEX msgs_msg_org_created_id_where_outbound_visible_outbox
ON msgs_msg(org_id, created_on DESC, id DESC)
WHERE direction = 'O' AND visibility = 'V' AND status IN ('P', 'Q');

CREATE INDEX msgs_msg_org_created_id_where_outbound_visible_sent
ON msgs_msg(org_id, created_on DESC, id DESC)
WHERE direction = 'O' AND visibility = 'V' AND status IN ('W', 'S', 'D');

CREATE INDEX msgs_msg_org_created_id_where_outbound_visible_failed
ON msgs_msg(org_id, created_on DESC, id DESC)
WHERE direction = 'O' AND visibility = 'V' AND status = 'F';

CREATE INDEX msgs_broadcasts_org_created_id_where_active
ON msgs_broadcast(org_id, created_on DESC, id DESC)
WHERE is_active = true;

CREATE INDEX msgs_msg_external_id_where_nonnull
ON msgs_msg(external_id)
WHERE external_id IS NOT NULL;
    """

    dependencies = [("msgs", "0076_install_triggers")]

    operations = [migrations.RunSQL(INDEX_SQL)]
