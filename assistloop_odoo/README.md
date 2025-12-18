# AssistLoop AI Chatbot for Odoo

Integrate the AssistLoop AI-powered customer support chatbot into your Odoo website.

## Overview

This Odoo module allows you to easily embed the AssistLoop AI chatbot on your Odoo-powered website. Once configured, your website visitors can interact with your AI agent for instant customer support.

## Features

- **Easy Configuration** - Set up through Odoo's Website Settings
- **Enable/Disable Toggle** - Turn the chatbot on/off without losing configuration
- **AI-Powered Support** - 24/7 automated customer support
- **Human Handoff** - Seamlessly transfer to human agents when needed
- **Compatible with Odoo 19.0**

## Requirements

- Odoo 19.0
- `website` module installed
- Valid AssistLoop account with a configured AI agent

## Installation

### Method 1: Odoo Apps Store (Recommended)

1. Go to **Apps** in your Odoo instance
2. Search for **"AssistLoop AI Chatbot"**
3. Click **Install**

### Method 2: Manual Installation

1. Download or clone this module to your Odoo addons directory:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/AssistLoop/Odoo.git
   ```

2. Restart Odoo server:
   ```bash
   sudo systemctl restart odoo
   ```

3. Update the apps list:
   - Go to **Apps** menu
   - Click **Update Apps List**
   - Search for "AssistLoop"

4. Install the module:
   - Click **Install** on "AssistLoop AI Chatbot"

### Method 3: Odoo.sh

1. Add the module to your repository's `addons` folder
2. Commit and push changes
3. The module will be available in Apps

## Configuration

1. Navigate to **Website → Configuration → Settings**

2. Scroll to the **AssistLoop AI Chatbot** section

3. Configure the following options:

   | Setting | Description |
   |---------|-------------|
   | **Enable Chat Widget** | Toggle to show/hide the chatbot |
   | **Agent ID** | Your AssistLoop Agent UUID (from AssistLoop dashboard) |
   | **Show on All Pages** | Display chatbot on every page |

4. Click **Save**

## Getting Your Agent ID

1. Log in to your [AssistLoop Dashboard](https://assistloop.ai/dashboard)
2. Select your organization
3. Navigate to your agent
4. Copy the Agent UUID from the agent settings

## Troubleshooting

### Widget not appearing

1. Verify the Agent ID is correct
2. Ensure "Enable Chat Widget" is turned on
3. Check browser console for errors
4. Clear Odoo cache: **Settings → Technical → Clear Cache**

### Widget loads but doesn't work

1. Verify your AssistLoop agent is properly configured
2. Check that the agent has training data
3. Ensure your AssistLoop subscription is active

## Technical Details

### Module Structure

```
assistloop_odoo/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── res_config_settings.py
├── views/
│   ├── res_config_settings_views.xml
│   └── templates.xml
├── data/
│   └── ir_config_parameter_data.xml
├── security/
│   └── ir.model.access.csv
└── static/
    ├── description/
    │   └── index.html
    └── src/
        └── js/
            └── assistloop_widget.js
```

### Configuration Parameters

The module stores configuration in `ir.config_parameter`:

| Key | Description |
|-----|-------------|
| `assistloop.enabled` | Widget enabled state |
| `assistloop.agent_id` | Agent UUID |
| `assistloop.show_on_all_pages` | Show on all pages flag |

### JavaScript API

The widget loader exposes methods via `window.AssistLoopLoader`:

```javascript
// Show the widget
AssistLoopLoader.show();

// Hide the widget
AssistLoopLoader.hide();

// Open chat window
AssistLoopLoader.open();

// Close chat window
AssistLoopLoader.close();
```

### Events

Listen for widget load completion:

```javascript
document.addEventListener('assistloop:loaded', function(e) {
    console.log('Widget loaded for agent:', e.detail.agentId);
});
```

## Support

- **Documentation**: [https://docs.assistloop.ai](https://docs.assistloop.ai)
- **Support Email**: support@assistloop.ai
- **Website**: [https://assistloop.ai](https://assistloop.ai)

## License

This module is licensed under LGPL-3. See [LICENSE](LICENSE) for details.

## Changelog

### Version 19.0.1.0.0

- Initial release for Odoo 19.0
- AI-powered chatbot integration
- Simple settings configuration
- Human handoff support
