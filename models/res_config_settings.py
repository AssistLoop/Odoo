# -*- coding: utf-8 -*-
"""
AssistLoop Configuration Settings
=================================

This module extends Odoo's res.config.settings to add AssistLoop-specific
configuration options for the chat widget.
"""

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """
    Extends the base configuration settings to include AssistLoop widget options.
    
    These settings are stored in ir.config_parameter and are accessible
    system-wide for configuring the AssistLoop chat widget behavior.
    """
    _inherit = 'res.config.settings'

    # AssistLoop Configuration Fields
    assistloop_agent_id = fields.Char(
        string='Agent ID',
        help='Enter the Agent UUID from your AssistLoop dashboard. '
             'This identifies which AI agent will power the chat widget.',
        config_parameter='assistloop.agent_id',
    )

    assistloop_enabled = fields.Boolean(
        string='Enable Chat Widget',
        help='Enable or disable the AssistLoop chat widget on your website. '
             'When disabled, the widget will not appear on any pages.',
        config_parameter='assistloop.enabled',
        default=False,
    )

    assistloop_position = fields.Selection(
        selection=[
            ('right', 'Bottom Right'),
            ('left', 'Bottom Left'),
        ],
        string='Widget Position',
        help='Choose where the chat widget button appears on your website.',
        config_parameter='assistloop.position',
        default='right',
    )

    assistloop_widget_url = fields.Char(
        string='Widget Script URL',
        help='Custom URL for the AssistLoop widget script. '
             'Leave empty to use the default CDN URL.',
        config_parameter='assistloop.widget_url',
    )

    assistloop_show_on_all_pages = fields.Boolean(
        string='Show on All Pages',
        help='When enabled, the widget appears on all website pages. '
             'When disabled, you can control visibility per page.',
        config_parameter='assistloop.show_on_all_pages',
        default=True,
    )

    @api.model
    def get_assistloop_config(self):
        """
        Retrieve the current AssistLoop configuration.
        
        This method is used by the frontend template to get the configuration
        values needed to initialize the chat widget.
        
        Returns:
            dict: Configuration dictionary containing:
                - agent_id: The AssistLoop agent UUID
                - enabled: Whether the widget is enabled
                - position: Widget button position ('left' or 'right')
                - widget_url: URL to load the widget script from
                - show_on_all_pages: Whether to show on all pages
        """
        IrConfigParam = self.env['ir.config_parameter'].sudo()
        
        return {
            'agent_id': IrConfigParam.get_param('assistloop.agent_id', ''),
            'enabled': IrConfigParam.get_param('assistloop.enabled', 'False') == 'True',
            'position': IrConfigParam.get_param('assistloop.position', 'right'),
            'widget_url': IrConfigParam.get_param(
                'assistloop.widget_url',
                'https://assistloop.ai/assistloop-widget.js'
            ),
            'show_on_all_pages': IrConfigParam.get_param(
                'assistloop.show_on_all_pages', 'True'
            ) == 'True',
        }

    def set_values(self):
        """
        Override to handle any custom logic when saving settings.
        """
        super().set_values()
        # Additional validation or processing can be added here
        # For example, validating the agent_id format

    @api.model
    def get_values(self):
        """
        Override to load AssistLoop settings values.
        """
        res = super().get_values()
        IrConfigParam = self.env['ir.config_parameter'].sudo()
        
        res.update({
            'assistloop_agent_id': IrConfigParam.get_param('assistloop.agent_id', ''),
            'assistloop_enabled': IrConfigParam.get_param('assistloop.enabled', 'False') == 'True',
            'assistloop_position': IrConfigParam.get_param('assistloop.position', 'right'),
            'assistloop_widget_url': IrConfigParam.get_param('assistloop.widget_url', ''),
            'assistloop_show_on_all_pages': IrConfigParam.get_param(
                'assistloop.show_on_all_pages', 'True'
            ) == 'True',
        })
        
        return res
