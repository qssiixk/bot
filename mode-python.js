define("ace/mode/python_highlight_rules", ["require", "exports", "module", "ace/lib/oop", "ace/mode/text_highlight_rules"], function (require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

    var PythonHighlightRules = function () {


        var builtinConstants = (
            "platform_id|client_id|api_key|messenger|name|full_name|custom_answer|wa_bot|question|attachments|" +
            "order|order_id|none|current_date|timestamp|date_of_creation|next_day|" +
            "message_id|current_time|weekday|attachment_url|client_type|avatar|group"
        );

        var builtinFunctions = (
            'sin|cos|tan|asin|acos|atan|sqrt|abs|ceil|floor|exp|random|fac|log|min|max|int|round|float|pyt|pow|atan2|concat|compareTime|compare_time|addDays|add_days|addMonth|add_month|addYear|add_year|addCols|add_cols|c2n|n2c|addMinutes|add_minutes|replace|compareDate|compare_date|weekday_date|month_date|add_unread|clear_unread|len|normalizePhone|proxy|proxy_timeout|proxy_date|short|short_timeout|short_date|substring|convert_datetime|get_datetime|base64|base64decode|md5|sha1|sha256|hmac_hexdigest|startswith|contains|endswith|if|find_client_id|inlist|some_client_in_list|create_list|add_to_list|add_to_list_by_list_name|list_size|list_size_by_list_name|lists_joint_count|move_to_list|move_to_list_by_list_name|sort|sort_by_value|remove_from_list|remove_from_list_by_list_name|clear_list|clear_list_by_list_name|create_list_if_not_exist|create_label_if_not_exist|days_from_last_message|unsubscribe|block_client|unblock_client|assign_to_user|distribute_client|free_client|get|set|except_arr|cross_arr|exist_key|sum_array|in_array|arr_len|key_index|humanize|append|insert|del|remove|index|urlencode|urldecode|findall|select_random|is_int|is_float|birthdate|lower|upper|capitalize|title|splitter|create_task|was_in_state|get_operator|get_operator_name|check_operator_status|done_task|update_task|delete_task|status_task|get_state_id|change_state|check_insta_subscription|check_vk_subscription|get_whatsapp_bot_id_by_phone|check_whatsapp|similar|strip|remove_last_message|last_message_id|last_messages_ids|distance|delete_pended_messages|delete_pended_messages_from_list|time_interval|shuffle_massive|massive_to_text|array_slice|count_occurrences|unpack_list|remove_duplicates|int_to_string|customizable_round_multiply|customizable_round_division|current_date_rus|date_rus|dict_keys_to_array|dict_values_to_array|tg_callback|whatsapp_message|get_block_name_by_id|callback|message|platform_message|send_unsubscribe_to_vtargete|send_subscribe_to_vtargete|send_unsubscribe_to_loktar|send_subscribe_to_loktar|send_carousel|set_note|set_client_name|set_client_var|set_client_vars|get_client_var|get_client_vars|get_active_orders_ids|get_success_orders_ids|get_fail_orders_ids|get_order_id|get_order_var|set_order_var|get_order_vars|set_order_vars|move_order_to_next_state|set_order_status_success|set_order_status_fail|set_order_status_archive|create_order|set_order_name|set_order_budget|create_label|add_label|remove_label|has_label|remove_label_everywhere|count_of_clients_with_label|get_all_client_labels|get_all_client_lists|remove_multiple_client_labels|remove_list_from_project|find_clients_by_multiple_labels|has_client_multiple_labels|tg_answer_callback_query|tg_send_document|tg_send_voice|tg_send_animation|tg_send_video|tg_send_venue|tg_send_contact|tg_send_sticker|tg_send_video_note|tg_send_photo|tg_send_media_group|tg_send_message|tg_send_message_1|tg_send_some_photo|tg_send_some_video|tg_send_some_document|tg_send_some_audio|tg_forward_message|tg_create_chat_invite_link|tg_revoke_chat_invite_link|tg_unban_chat_member|tg_ban_chat_member|tg_restrict_chat_member|tg_approve_chat_join_request|tg_decline_chat_join_request|tg_get_chat_member|tg_delete_message|tg_delete_messages|tg_edit_message_text|tg_edit_message_caption|tg_edit_message_media|tg_edit_message_reply_markup|tg_send_poll|tg_send_quiz_poll|tg_stop_poll|tg_send_invoice|tg_escape|tg_add_thanks_score|tg_add_thanks_score_for_answer|tg_minus_thanks_score|tg_get_user_info|tg_get_top|tg_mark_ban_user|tg_mark_unban_user|tg_previous_next_rating_buttons|tg_get_chat_member_count|tg_send_chat_action|tg_chat_permission|tg_export_chat_link|tg_pin_chat_message|tg_unpin_chat_message|tg_unpin_all|tg_set_chat_photo|tg_delete_chat_photo|tg_set_command|tg_get_command|tg_delete_command|tg_set_chat_menu_button|tg_send_dice|tg_callback_url_open|tg_promote_user|tg_set_administrator_title|tg_set_group_title|tg_set_chat_description|tg_ban_chat_sender_chat|tg_unban_chat_sender_chat|tg_copy_message|tg_get_forum_icon|tg_create_forum_topic|tg_edit_forum_topic|tg_close_forum_topic|tg_reopen_forum_topic|tg_delete_forum_topic|tg_unpin_topic_messages|tg_edit_general_forum_topic|tg_close_general_forum_topic|tg_reopen_general_forum_topic|tg_hide_general_forum_topic|tg_unhide_general_forum_topic|tg_set_bot_description|tg_get_bot_description|tg_set_bot_short_description|tg_get_bot_short_description|tg_set_reaction|vk_create_comment|vk_get_name|vk_send_message|vk_send_sticker|vk_send_some_photo|vk_remove_chat_user|vk_approve_request|vk_delete_last_message|vk_add_to_target_group|vk_remove_from_target_group|vk_add_new_target_group|vk_add_thanks_score|vk_minus_thanks_score|vk_get_top|vk_mark_ban_user|vk_mark_unban_user|vk_get_user_link|vk_pin_message|vk_unpin_message|vk_send_chat_action|vk_get_chat_member_count|vk_export_chat_link|vk_delete_messages|vk_mark_conversation|vk_unmark_conversation|vk_ban_by_id|vk_unban_by_id|vk_remove_group_user|vk_edit_manager|vk_edit_message|vk_get_short_link|vk_show_alert_message|vk_callback_url|vk_search_message|vk_open_comment|vk_close_comment|vk_liked_object|vk_create_wall_post|vk_delete_wall_post_comment|vk_send_message_reaction|vk_delete_message_reaction|vk_get_message_reactions|vk_get_wall_watch_count|vk_ord_upload_media|vk_ord_create_counteragent|vk_ord_add_contract|vk_ord_add_pad|vk_ord_add_invoice|vk_ord_add_creative|vk_ord_create_new_publisher|vk_ord_add_new_distribution|vk_ord_add_web_pad|vk_ord_add_new_creative|vk_ord_create_invoice|vk_check_user_online|wildberries_goods_feedbacks|wildberries_answer_to_feedback|wildberries_questions|wildberries_question_mark_viewed|wildberries_answer_question|ozon_goods_feedbacks|vk_vision_recognize_text|robokassa_recurrent_payment|cloudpayments_subscription_info|cloudpayments_update_subscription|cloudpayments_remove_subscription|cloudpayments_token_payment|prodamus_subscription_discount|prodamus_subscription_switch_status|prodamus_subscription_payment_date|coinpayments_get_payment_status|tinkoff_recurrent_payment|tinkoff_sm_register_get_token|tinkoff_sm_register_get_shop_code|payeer_function|amo_change_state|amo_get_lead_info|amo_get_lead_custom_field|amo_get_contact_info|amo_get_contact_custom_field|amo_create_task|amo_set_tags|amo_set_budget|amo_set_lead_name|amo_set_lead_responsible_user|amo_set_contact_responsible_user|amo_add_notes|amo_add_contact_notes|amo_get_token|amo_add_lead_custom_fields|amo_add_contact_custom_fields|amo_set_contact_name|amo_add_lead|bitrix_add_comment|bitrix_add_deal_comment|bitrix_add_contact_comment|bitrix_add_lead_comment|bitrix_deal_responsible|bitrix_contact_responsible|bitrix_lead_responsible|bitrix_deal_fields|bitrix_contact_fields|bitrix_lead_fields|bitrix_deal_search|bitrix_contact_search|bitrix_lead_search|bitrix_product_search|bitrix_dialog_finish|bizon365_add_subscriber|bizon365_is_visitor|getcourse_add_user|getcourse_add_deal|getcourse_update_deal|getcourse_change_deal_status|getcourse_add_user_to_groups|myownconference_find_webinars|myownconference_history_user|myownconference_is_online_user|myownconference_is_our_user|myownconference_add_user|myownconference_add_user_to_webinar|webinargeek_get_webinar_list|webinargeek_add_subscriber|webinargeek_is_visitor|webinargeek_search_broadcast_id|klientiks_get_employees_list|klientiks_get_services_list|klientiks_get_free_date_for_record|klientiks_add_record_for_client|klientiks_add_new_clients|klientiks_get_times|klientiks_visit_cancel|inxy_remove_subscription|stripe_add_subscription_discount|stripe_remove_subscription_discount|stripe_remove_subscription|stripe_check_subscription|lava_check_payment_status|paypal_payment_url|paypal_subscription_url|paypal_remove_subscription|paypal_subscription_data|tinkoff_credit_create_invoice|tinkoff_credit_action|tinkoff_credit_info|life_pay_get_token|life_pay_recurrent_payment|life_pay_refund_payment|life_pay_stop_recurrent_payments|life_pay_get_payment_info|allpay_generate_payment_url|wallet_pay_generate_payment_url|paykeeper_generate_payment_url|mandarin_generate_payment_url|mandarin_get_order_info|uiscom_scenario_call|uiscom_employee_call|uiscom_offline_messages|uiscom_get_sites|uiscom_get_campaigns|sipuni_scheme_call|sipuni_internal_to_external_call|mango_employee_call|mango_group_call|iptelefon_employee_call|iptelefon_group_call|zadarma_call|zvonobot_call|zvonobot_digits_call|telphin_employee_call|telphin_group_call|onlinepbx_employee_call|onlinepbx_group_call|megafon_call|ga4_event|ga_pageview|ga_event|ga_transaction_pageview|ga_transaction_event|ym_create_js_event_goal|ym_send_offline_conversions|ym_info_about_goals|insta_create_comment|like_client_message|reply_to_mention|comment_text|ig_set_persistent_menu|ig_delete_persistent_menu|fb_set_persistent_menu|fb_delete_persistent_menu|sendpulse_email|sendpulse_email_template|sendpulse_add_to_addressbook|sendpulse_sms|send_email|remove_links|remove_one_time_links|remove_timer_links|moysklad_get_goods|moysklad_make_order|moysklad_humanize_goods_list|moysklad_get_goods_photo|moysklad_get_organizations|moysklad_get_sale_channels|moysklad_get_projects|moysklad_get_storages|game_add_comment|game_add_stories|game_add_message|game_add_stories_mention|game_add_post_mention|game_get_user_score|game_get_user_place|game_get_leader_score|game_get_top|game_add_score|game_set_score|game_add_value|game_set_value|game_ban_player|game_unban_player|game_user_banned|game_minus_user_score|game_get_today_user_comment_action|game_get_today_user_message_actions|game_get_today_user_stories_actions|game_get_today_user_post_mention_actions|game_get_today_user_stories_mention_actions|game_get_total_comment_action|game_get_total_message_actions|game_get_total_stories_actions|game_get_total_stories_mention_actions|game_get_total_post_mention_actions|tools_make_button_str_checker|tools_check_user_input|sheet_create_worksheet|sheet_mapping_cells|sheet_append_row|sheet_write_cells|sheet_remove_cells|sheet_read_cells|sheet_append_cell_in_row|sheet_add_to_acell|sheet_add_to_cell|sheet_sub_to_acell|sheet_sub_to_cell|sheet_mul_to_acell|sheet_mul_to_cell|sheet_div_to_acell|sheet_div_to_cell|sheet_append_to_acell|sheet_append_to_cell|sheet_remove_row|sheet_remove_col|sheet_remove_range|sheet_search_in_col_return_cell|sheet_search_in_col_return_row|sheet_search_in_col_return_cells_list|sheet_search_in_multiple_cols_return_list|sheet_search_in_multiple_cols_return_row|sheet_create_spreadsheet|sheet_copy_list|sheet_search_in_col_return_row_array|sheet_copy_data_block|sheet_search_in_col_write_cells|sheet_search_in_all_sheets|sheet_delete_worksheet|sheet_worksheet_indexes|sheet_rename_worksheet|gd_create_new_doc|gd_replace_text|gd_add_text|gd_copy|gd_add_image|save_google_doc|code_executor|get_main_id|unmerge_client|merge_client|get_merge_link|get_bind_clients|quiz_link_timeout|quiz_link_date|quiz_link|set_inline_menu_from_sheet|get_client_id_by_platform_id|confirm_email_subscription|send_email_template|send_email_from_bot|open_ai_create_completion|open_ai_moderations|open_ai_edits|open_ai_images_generations|open_ai_chat_completions|open_ai_thread_create|open_ai_thread_add_message|open_ai_thread_run|open_ai_thread_get_messages|get_robokassa_payment_url|get_yookassa_payment_url|get_cloudpayments_payment_url|get_cloudpayments_uz_payment_url|get_life_pay_payment_url|get_tinkoff_payment_url|get_prodamus_payment_url|get_prodamus_subscription_url|register_customer_on_course|register_customer|del_customer_from_course|has_customer_tariff|has_customer_tariff_with_date|access_course_from_webapp|customer_was_on_translation|get_certificate|get_custom_image|online_chat_send_form|requests_post|requests_get|requests_put|requests_patch|requests_delete|get_companies_for_booking|get_categories_for_booking|get_employees_for_booking|get_services_for_booking|get_dates_for_booking|get_slots_for_booking|get_info_for_booking|get_info_from_table|create_booking|create_booking_by_name|get_bookings_info|get_active_order_booking_info|modify_booking_time|cancel_booking|count_client_orders|latest_order_datetime|get_order_id_by_var_value|get_count_orders|get_bepaid_subscription_url|get_bepaid_subscription_info|cancel_bepaid_subscription|make_bepaid_token_payment|payselection_create_pay_url|payselection_create_subscription_pay|payselection_cancel_subscription|pause_bot|ai_context_answer|clear_assistant_chat_history'
        )
        var keywordMapper = this.createKeywordMapper({
            "function": builtinFunctions,
            "constant": builtinConstants
        }, "identifier");

        var escapedChars = "\\\\(?:n(?:[1-7][0-7]{0,2}|0)|[nsrtvfbae'\"\\\\]|c(?:\\\\M-)?.|M-(?:\\\\C-|\\\\c)?.|C-(?:\\\\M-)?.|[0-7]{3}|x[\\da-fA-F]{2}|u[\\da-fA-F]{4}|u{[\\da-fA-F]{1,6}(?:\\s[\\da-fA-F]{1,6})*})";

        var constantOtherSymbol = exports.constantOtherSymbol = {
            token : "constant.other.symbol.ruby", // symbol
            regex : "[:](?:[A-Za-z_]|[@$](?=[a-zA-Z0-9_]))[a-zA-Z0-9_]*[!=?]?"
        };

        exports.qString = {
            token : "string", // single line
            regex : "['](?:(?:\\\\.)|(?:[^'\\\\]))*?[']"
        };

        exports.qqString = {
            token : "string", // single line
            regex : '["](?:(?:\\\\.)|(?:[^"\\\\]))*?["]'
        };

        exports.tString = {
            token : "string", // backtick string
            regex : "[`](?:(?:\\\\.)|(?:[^'\\\\]))*?[`]"
        };

        var constantNumericDecimal = exports.constantNumericDecimal = {
            token: "constant.numeric",
            regex: /\b(0[dD](?:[1-9](?:[\d]|_(?=[\d]))*|0))\b/
        };

        var constantNumericFloat = exports.constantNumericFloat = {
            token : "constant.numeric", // float + complex
            regex : "[+-]?\\d(?:\\d|_(?=\\d))*(?:(?:\\.\\d(?:\\d|_(?=\\d))*)?(?:[eE][+-]?\\d+)?)?i?\\b"
        };
        this.$rules = {
            "start": [
                [{
                    token: "comment",
                    regex: /(\n|^)\/\*/,
                    next: [
                        {
                            token: "comment",
                            regex: /\*\/(\n|$)/,
                            next: "start"
                        }, {
                            defaultToken: "comment"
                        }
                    ]
                }, {
                    token: ["constant.other.symbol.ruby", "string.start"],
                    regex: /(:)?(")/,
                    push: [{
                        token: "constant.language.escape",
                        regex: escapedChars
                    }, {
                        token: "paren.start",
                        regex: /#{/,
                        push: "start"
                    }, {
                        token: "string.end",
                        regex: /"/,
                        next: "pop"
                    }, {
                        defaultToken: "string"
                    }]
                }, {
                    token: "string.start",
                    regex: /`/,
                    push: [{
                        token: "constant.language.escape",
                        regex: escapedChars
                    }, {
                        token: "paren.start",
                        regex: /#{/,
                        push: "start"
                    }, {
                        token: "string.end",
                        regex: /`/,
                        next: "pop"
                    }, {
                        defaultToken: "string"
                    }]
                }, {
                    token: ["constant.other.symbol.ruby", "string.start"],
                    regex: /(:)?(')/,
                    push: [{
                        token: "constant.language.escape",
                        regex: /\\['\\]/
                    }, {
                        token: "string.end",
                        regex: /'/,
                        next: "pop"
                    }, {
                        defaultToken: "string"
                    }]
                }, {
                    token: "string.start",//doesn't see any differences between strings and array of strings in highlighting
                    regex: /%[qwx]([(\[<{^|%])/, onMatch: function (val, state, stack) {
                        if (stack.length)
                            stack = [];
                        var paren = val[val.length - 1];
                        stack.unshift(paren, state);
                        this.next = "qStateWithoutInterpolation";
                        return this.token;
                    }
                }, {
                    token: "string.start", //doesn't see any differences between strings and array of strings in highlighting
                    regex: /%[QWX]?([(\[<{^|%])/, onMatch: function (val, state, stack) {
                        if (stack.length)
                            stack = [];
                        var paren = val[val.length - 1];
                        stack.unshift(paren, state);
                        this.next = "qStateWithInterpolation";
                        return this.token;
                    }
                }, {
                    token: "constant.other.symbol.ruby", //doesn't see any differences between symbols and array of symbols in highlighting
                    regex: /%[si]([(\[<{^|%])/, onMatch: function (val, state, stack) {
                        if (stack.length)
                            stack = [];
                        var paren = val[val.length - 1];
                        stack.unshift(paren, state);
                        this.next = "sStateWithoutInterpolation";
                        return this.token;
                    }
                }, {
                    token: "constant.other.symbol.ruby", //doesn't see any differences between symbols and array of symbols in highlighting
                    regex: /%[SI]([(\[<{^|%])/, onMatch: function (val, state, stack) {
                        if (stack.length)
                            stack = [];
                        var paren = val[val.length - 1];
                        stack.unshift(paren, state);
                        this.next = "sStateWithInterpolation";
                        return this.token;
                    }
                }, {
                    token: "string.regexp",
                    regex: /%[r]([(\[<{^|%])/, onMatch: function (val, state, stack) {
                        if (stack.length)
                            stack = [];
                        var paren = val[val.length - 1];
                        stack.unshift(paren, state);
                        this.next = "rState";
                        return this.token;
                    }
                }],

                {
                    token: ["punctuation.operator", "support.function"],
                    regex: /(\.)([a-zA-Z_\d]+)(?=\()/
                }, {
                    token: ["punctuation.operator", "identifier"],
                    regex: /(\.)([a-zA-Z_][a-zA-Z_\d]*)/
                }, {
                    token: "string.character",
                    regex: "\\B\\?(?:" + escapedChars + "|\\S)"
                }, {
                    token: "punctuation.operator",
                    regex: /\?(?=.+:)/
                },

                constantOtherSymbol,
                constantNumericFloat,
                constantNumericDecimal,
                {
                    token: "constant.language.boolean",
                    regex: "(True|False|None)\\b"
                }, {
                    token: keywordMapper,
                    regex: "[a-zA-Z_$][a-zA-Z0-9_$]*\\b"
                }, {
                    regex: "$",
                    token: "empty",
                    next: function (currentState, stack) {
                        if (stack[0] === "heredoc" || stack[0] === "indentedHeredoc")
                            return stack[0];
                        return currentState;
                    }
                }, {
                    token: "keyword.operator",
                    regex: "!|\\$|%|&|\\*|/|\\-\\-|\\-|\\+\\+|\\+|~|===|==|=|!=|!==|<=|>=|<>|<|>|!|&&|AND|and|or|OR|\\|\\||\\?\\:|\\*=|%=|\\+=|\\-=|&=|\\^=|\\|"
                }, {
                    token: "paren.lparen",
                    regex: "[[({]"
                }, {
                    token: "paren.rparen",
                    regex: "[\\])}]",
                    onMatch: function (value, currentState, stack) {
                        this.next = '';
                        if (value == "}" && stack.length > 1 && stack[1] != "start") {
                            stack.shift();
                            this.next = stack.shift();
                        }
                        return this.token;
                    }
                }, {
                    token: "text",
                    regex: "\\s+"
                }, {
                    token: "punctuation.operator",
                    regex: /[?:,;.]/
                }
            ],
            "qStateWithInterpolation": [{
                token: "string.start",// excluded nested |^% due to difficulty in realization
                regex: /[(\[<{]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === stack[0]) {
                        stack.unshift(val, state);
                        return this.token;
                    }
                    return "string";
                }
            }, {
                token: "constant.language.escape",
                regex: escapedChars
            }, {
                token: "constant.language.escape",
                regex: /\\./
            }, {
                token: "paren.start",
                regex: /#{/,
                push: "start"
            }, {
                token: "string.end",
                regex: /[)\]>}^|%]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === closeParen[stack[0]]) {
                        stack.shift();
                        this.next = stack.shift();
                        return this.token;
                    }
                    this.next = '';
                    return "string";
                }
            }, {
                defaultToken: "string"
            }],
            "qStateWithoutInterpolation": [{
                token: "string.start",// excluded nested |^% due to difficulty in realization
                regex: /[(\[<{]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === stack[0]) {
                        stack.unshift(val, state);
                        return this.token;
                    }
                    return "string";
                }
            }, {
                token: "constant.language.escape",
                regex: /\\['\\]/
            }, {
                token: "constant.language.escape",
                regex: /\\./
            }, {
                token: "string.end",
                regex: /[)\]>}^|%]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === closeParen[stack[0]]) {
                        stack.shift();
                        this.next = stack.shift();
                        return this.token;
                    }
                    this.next = '';
                    return "string";
                }
            }, {
                defaultToken: "string"
            }],
            "sStateWithoutInterpolation": [{
                token: "constant.other.symbol.ruby",// excluded nested |^% due to difficulty in realization
                regex: /[(\[<{]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === stack[0]) {
                        stack.unshift(val, state);
                        return this.token;
                    }
                    return "constant.other.symbol.ruby";
                }
            }, {
                token: "constant.other.symbol.ruby",
                regex: /[)\]>}^|%]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === closeParen[stack[0]]) {
                        stack.shift();
                        this.next = stack.shift();
                        return this.token;
                    }
                    this.next = '';
                    return "constant.other.symbol.ruby";
                }
            }, {
                defaultToken: "constant.other.symbol.ruby"
            }],
            "sStateWithInterpolation": [{
                token: "constant.other.symbol.ruby",// excluded nested |^% due to difficulty in realization
                regex: /[(\[<{]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === stack[0]) {
                        stack.unshift(val, state);
                        return this.token;
                    }
                    return "constant.other.symbol.ruby";
                }
            }, {
                token: "constant.language.escape",
                regex: escapedChars
            }, {
                token: "constant.language.escape",
                regex: /\\./
            }, {
                token: "paren.start",
                regex: /#{/,
                push: "start"
            }, {
                token: "constant.other.symbol.ruby",
                regex: /[)\]>}^|%]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === closeParen[stack[0]]) {
                        stack.shift();
                        this.next = stack.shift();
                        return this.token;
                    }
                    this.next = '';
                    return "constant.other.symbol.ruby";
                }
            }, {
                defaultToken: "constant.other.symbol.ruby"
            }],
            "rState": [{
                token: "string.regexp",// excluded nested |^% due to difficulty in realization
                regex: /[(\[<{]/, onMatch: function (val, state, stack) {
                    if (stack.length && val === stack[0]) {
                        stack.unshift(val, state);
                        return this.token;
                    }
                    return "constant.language.escape";
                }
            }, {
                token: "paren.start",
                regex: /#{/,
                push: "start"
            }, {
                token: "string.regexp",
                regex: /\//
            }, {
                token: "string.regexp",
                regex: /[)\]>}^|%][imxouesn]*/, onMatch: function (val, state, stack) {
                    if (stack.length && val[0] === closeParen[stack[0]]) {
                        stack.shift();
                        this.next = stack.shift();
                        return this.token;
                    }
                    this.next = '';
                    return "constant.language.escape";
                }
            },
                {include: "regex"},
                {
                    defaultToken: "string.regexp"
                }],
            "regex": [
                {// character classes
                    token: "regexp.keyword",
                    regex: /\\[wWdDhHsS]/
                }, {
                    token: "constant.language.escape",
                    regex: /\\[AGbBzZ]/
                }, {
                    token: "constant.language.escape",
                    regex: /\\g<[a-zA-Z0-9]*>/
                }, {
                    token: ["constant.language.escape", "regexp.keyword", "constant.language.escape"],
                    regex: /(\\p{\^?)(Alnum|Alpha|Blank|Cntrl|Digit|Graph|Lower|Print|Punct|Space|Upper|XDigit|Word|ASCII|Any|Assigned|Arabic|Armenian|Balinese|Bengali|Bopomofo|Braille|Buginese|Buhid|Canadian_Aboriginal|Carian|Cham|Cherokee|Common|Coptic|Cuneiform|Cypriot|Cyrillic|Deseret|Devanagari|Ethiopic|Georgian|Glagolitic|Gothic|Greek|Gujarati|Gurmukhi|Han|Hangul|Hanunoo|Hebrew|Hiragana|Inherited|Kannada|Katakana|Kayah_Li|Kharoshthi|Khmer|Lao|Latin|Lepcha|Limbu|Linear_B|Lycian|Lydian|Malayalam|Mongolian|Myanmar|New_Tai_Lue|Nko|Ogham|Ol_Chiki|Old_Italic|Old_Persian|Oriya|Osmanya|Phags_Pa|Phoenician|Rejang|Runic|Saurashtra|Shavian|Sinhala|Sundanese|Syloti_Nagri|Syriac|Tagalog|Tagbanwa|Tai_Le|Tamil|Telugu|Thaana|Thai|Tibetan|Tifinagh|Ugaritic|Vai|Yi|Ll|Lm|Lt|Lu|Lo|Mn|Mc|Me|Nd|Nl|Pc|Pd|Ps|Pe|Pi|Pf|Po|No|Sm|Sc|Sk|So|Zs|Zl|Zp|Cc|Cf|Cn|Co|Cs|N|L|M|P|S|Z|C)(})/
                }, {
                    token: ["constant.language.escape", "invalid", "constant.language.escape"],
                    regex: /(\\p{\^?)([^/]*)(})/
                }, {// escapes
                    token: "regexp.keyword.operator",
                    regex: "\\\\(?:u[\\da-fA-F]{4}|x[\\da-fA-F]{2}|.)"
                }, {// flag
                    token: "string.regexp",
                    regex: /[/][imxouesn]*/,
                    next: "start"
                }, {// invalid operators
                    token: "invalid",
                    regex: /\{\d+\b,?\d*\}[+*]|[+*$^?][+*]|[$^][?]|\?{3,}/
                }, {// operators
                    token: "constant.language.escape",
                    regex: /\(\?(?:[:=!>]|<'?[a-zA-Z]*'?>|<[=!])|\)|\{\d+\b,?\d*\}|[+*]\?|[()$^+*?.]/
                }, {
                    token: "constant.language.delimiter",
                    regex: /\|/
                }, {
                    token: "regexp.keyword",
                    regex: /\[\[:(?:alnum|alpha|blank|cntrl|digit|graph|lower|print|punct|space|upper|xdigit|word|ascii):\]\]/
                }, {
                    token: "constant.language.escape",
                    regex: /\[\^?/,
                    push: "regex_character_class"
                }, {
                    defaultToken: "string.regexp"
                }
            ],
            "regex_character_class": [
                {
                    // character classes
                    token: "regexp.keyword",
                    regex: /\\[wWdDhHsS]/
                }, {
                    token: "regexp.charclass.keyword.operator",
                    regex: "\\\\(?:u[\\da-fA-F]{4}|x[\\da-fA-F]{2}|.)"
                }, {
                    token: "constant.language.escape",
                    regex: /&?&?\[\^?/,
                    push: "regex_character_class"
                }, {
                    token: "constant.language.escape",
                    regex: "]",
                    next: "pop"
                }, {
                    token: "constant.language.escape",
                    regex: "-"
                }, {
                    defaultToken: "string.regexp.characterclass"
                }
            ]
        };

        this.normalizeRules();
    };


    oop.inherits(PythonHighlightRules, TextHighlightRules);

    exports.PythonHighlightRules = PythonHighlightRules;
});

define("ace/mode/folding/pythonic", ["require", "exports", "module", "ace/lib/oop", "ace/mode/folding/fold_mode"], function (require, exports, module) {
    "use strict";

    var oop = require("../../lib/oop");
    var BaseFoldMode = require("./fold_mode").FoldMode;

    var FoldMode = exports.FoldMode = function (markers) {
        this.foldingStartMarker = new RegExp("([\\[{])(?:\\s*)$|(" + markers + ")(?:\\s*)(?:#.*)?$");
    };
    oop.inherits(FoldMode, BaseFoldMode);

    (function () {

        this.getFoldWidgetRange = function (session, foldStyle, row) {
            var line = session.getLine(row);
            var match = line.match(this.foldingStartMarker);
            if (match) {
                if (match[1])
                    return this.openingBracketBlock(session, match[1], row, match.index);
                if (match[2])
                    return this.indentationBlock(session, row, match.index + match[2].length);
                return this.indentationBlock(session, row);
            }
        };

    }).call(FoldMode.prototype);

});

define("ace/mode/python", ["require", "exports", "module", "ace/lib/oop", "ace/mode/text", "ace/mode/python_highlight_rules", "ace/mode/folding/pythonic", "ace/range"], function (require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextMode = require("./text").Mode;
    var PythonHighlightRules = require("./python_highlight_rules").PythonHighlightRules;
    var PythonFoldMode = require("./folding/pythonic").FoldMode;
    var Range = require("../range").Range;

    var Mode = function () {
        this.HighlightRules = PythonHighlightRules;
        this.foldingRules = new PythonFoldMode("\\:");
        this.$behaviour = this.$defaultBehaviour;
    };
    oop.inherits(Mode, TextMode);

    exports.Mode = Mode;
});
(function () {
    window.require(["ace/mode/python"], function (m) {
        if (typeof module == "object" && typeof exports == "object" && module) {
            module.exports = m;
        }
    });
})();
            