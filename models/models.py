# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clase_empresas_contratadoras(models.Model):
        _name = 'clase.empresas_contratadoras'
        _description = 'clase.empresas_contratadoras'

        name = fields.Char(string="Nombre Empresa")
        precio_bruto = fields.Float(string="Precio Bruto")
        precio_impuestos = fields.Float(string="Precio total con impuestos solo IGIC", compute="_precioimpuestos", store=True)
        proyecto = fields.Many2many("project.project",string="Proyecto",required=True)

        @api.depends('precio_bruto')
        def _precioimpuestos(self):
                for r in self:
                        r.precio_impuestos = r.precio_bruto*1.07

class clase_proyecto(models.Model):
        _name : 'project.project'
        _inherit : 'project.project'

        empresa_contratadora = fields.Many2one("clase.empresas_contratadoras",string="Empresa Contratadora",inverse_name="proyecto")
        tareas = fields.One2many('project.task', "project_id", string="Tareas")
