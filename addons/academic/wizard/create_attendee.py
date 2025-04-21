from odoo import api, fields, models

class CreateAttendeeWizard(models.TransientModel):
    _name = 'academic.create.attendee.wizard'

    session_id = fields.Many2one(
        comodel_name='academic.session',
        string="Session",
        #required=True      dihilangkan supaya bisa tetap confirm meski kosong
    )

    session_ids = fields.Many2many(
        comodel_name='academic.session',
        string="Sessions",
    )

    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        string="Partners to add to session",
        required=True
    )

    def action_add_attendee(self):
        self.ensure_one() #satu record

        #untuk bisa nambah ke banyak session
        for ses in self.session_ids:
            #one2many
            ses.attendee_ids = [(0,0,{
                'name': p.id,
                'partner_id': p.id
            }) for p in self.partner_ids ]

        # self.partner_ids = res.partner(1,2,3)
        #

        return {'type': 'ir.actions.act_window_close'}