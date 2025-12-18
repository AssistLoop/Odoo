/**
 * AssistLoop Widget Loader for Odoo
 * ==================================
 * 
 * This script handles the dynamic loading and initialization of the AssistLoop
 * chat widget on Odoo website pages. It reads configuration from the global
 * AssistLoopConfig object set by the Odoo backend template.
 * 
 * @author AssistLoop
 * @version 1.0.0
 * @license LGPL-3
 */

(function () {
    'use strict';

    /**
     * AssistLoop Widget Loader Module
     * Handles all widget initialization logic
     */
    const AssistLoopLoader = {
        /**
         * Default configuration values
         */
        defaults: {
            widgetUrl: 'https://cdn.assistloop.ai/widget/v1/assistloop-widget.js',
            position: 'right',
            retryAttempts: 3,
            retryDelay: 1000,
        },

        /**
         * Current configuration (merged with defaults)
         */
        config: null,

        /**
         * Track initialization state
         */
        initialized: false,

        /**
         * Initialize the widget loader
         * Reads configuration and loads the widget script
         */
        init: function () {
            if (this.initialized) {
                console.warn('[AssistLoop] Widget already initialized');
                return;
            }

            // Get configuration from global object set by Odoo template
            const globalConfig = window.AssistLoopConfig || {};

            // Validate required configuration
            if (!globalConfig.agentId) {
                console.warn('[AssistLoop] No agent ID configured. Widget will not load.');
                return;
            }

            // Merge with defaults
            this.config = {
                agentId: globalConfig.agentId,
                position: globalConfig.position || this.defaults.position,
                widgetUrl: globalConfig.widgetUrl || this.defaults.widgetUrl,
            };

            // Load the widget
            this.loadWidget();
        },

        /**
         * Load the AssistLoop widget script
         * @param {number} attempt - Current retry attempt number
         */
        loadWidget: function (attempt = 1) {
            const self = this;

            // Create script element
            const script = document.createElement('script');
            script.type = 'text/javascript';
            script.async = true;
            script.src = this.config.widgetUrl;

            // Set data attributes for widget configuration
            script.setAttribute('data-agent-id', this.config.agentId);
            script.setAttribute('data-position', this.config.position);

            // Handle successful load
            script.onload = function () {
                self.initialized = true;
                self.onWidgetLoaded();
            };

            // Handle load errors with retry logic
            script.onerror = function () {
                console.error('[AssistLoop] Failed to load widget script (attempt ' + attempt + ')');

                if (attempt < self.defaults.retryAttempts) {
                    console.log('[AssistLoop] Retrying in ' + self.defaults.retryDelay + 'ms...');
                    setTimeout(function () {
                        self.loadWidget(attempt + 1);
                    }, self.defaults.retryDelay);
                } else {
                    console.error('[AssistLoop] Max retry attempts reached. Widget failed to load.');
                }
            };

            // Append script to document
            const firstScript = document.getElementsByTagName('script')[0];
            if (firstScript && firstScript.parentNode) {
                firstScript.parentNode.insertBefore(script, firstScript);
            } else {
                document.head.appendChild(script);
            }
        },

        /**
         * Called when widget script has loaded successfully
         * Can be used to perform additional initialization
         */
        onWidgetLoaded: function () {
            console.log('[AssistLoop] Widget loaded successfully');

            // Dispatch custom event for any listeners
            const event = new CustomEvent('assistloop:loaded', {
                detail: {
                    agentId: this.config.agentId,
                    position: this.config.position,
                },
            });
            document.dispatchEvent(event);
        },

        /**
         * Manually show the widget (if supported by AssistLoop widget API)
         */
        show: function () {
            if (window.AssistLoop && typeof window.AssistLoop.show === 'function') {
                window.AssistLoop.show();
            }
        },

        /**
         * Manually hide the widget (if supported by AssistLoop widget API)
         */
        hide: function () {
            if (window.AssistLoop && typeof window.AssistLoop.hide === 'function') {
                window.AssistLoop.hide();
            }
        },

        /**
         * Open the chat window (if supported by AssistLoop widget API)
         */
        open: function () {
            if (window.AssistLoop && typeof window.AssistLoop.open === 'function') {
                window.AssistLoop.open();
            }
        },

        /**
         * Close the chat window (if supported by AssistLoop widget API)
         */
        close: function () {
            if (window.AssistLoop && typeof window.AssistLoop.close === 'function') {
                window.AssistLoop.close();
            }
        },
    };

    /**
     * Initialize when DOM is ready
     */
    function onDOMReady(callback) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', callback);
        } else {
            callback();
        }
    }

    // Start initialization when DOM is ready
    onDOMReady(function () {
        AssistLoopLoader.init();
    });

    // Expose loader to global scope for external access
    window.AssistLoopLoader = AssistLoopLoader;

})();
