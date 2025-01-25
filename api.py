import csv
import requests
import os

from dotenv import load_dotenv

import dto

load_dotenv()

headers = {
    'Host': 'api.lenta.com',
    'Timestamp': '1737614884',
    'X-Device-Brand': 'iPhone',
    'MarketingPartnerKey': 'mp403-3a8bc38112eecfff5936dc001481afe3',
    'baggage': 'sentry-environment=production,sentry-public_key=5a0ed5107ed94f37b4277e42af41260d,sentry-release=6.23.0,sentry-trace_id=b8af142fc89b4ae09e0626b06f5dda92',
    'X-Device-OS-Version': '14.8.1',
    'Accept': 'application/json',
    'DeviceId': os.getenv('DEVICE_ID'),
    'Created': '2025-01-23 09:48:05',
    'User-Agent': 'lo, 6.23.0',
    'Att': '3',
    'LocalTime': '2025-01-23T11:48:05+05:00',
    'X-Device-Name': 'iPhone9,3',
    'X-Retail-Brand': 'lo',
    'PassportAccessToken': os.getenv('PASSPORT_ACCESS_TOKEN'),
    'Client': 'ios_14.8.1_6.23.0',
    'Qrator-Token': os.getenv('QRATOR_TOKEN'),
    'RequestId': os.getenv('REQUEST_ID'),
    'Accept-Language': 'ru;q=1.0',
    'Method': 'catalogItemsListing',
    'sentry-trace': 'b8af142fc89b4ae09e0626b06f5dda92-06014df281824071-0',
    'X-Platform': 'omniapp',
    'Adid': os.getenv('AD_ID'),
    'X-Device-OS': 'iOS',
    'X-Delivery-Mode': 'shop',
    'AdvertisingId': os.getenv('ADVERTISING_ID'),
    'Content-Type': 'application/json',
    'SessionToken': os.getenv('SESSION_TOKEN'),
    'App-Version': '6.23.0',
    'AuthToken': os.getenv('AUTH_TOKEN'),
    'X-Device-id': os.getenv('X_DEVICE_ID'),
    'Experiments': 'exp_cardOne_available.test, exp_tips.test, exp_deducting_points.test, exp_email_optional_full_registration.test, exp_email_pop_up_enabled.false, exp_recommendation_cms.false, exp_search.new, exp_fullscreen.test, exp_ui_catalog.test, exp_newui_cancel_order.test, exp_description_payment_type.test, exp_newui_pdp.test, exp_lentapay.test, exp_address_intercom.test, exp_search_category_by_query.test, exp_new_empty_cart.test_unlimited_recommendation, exp_selection_carousel.control, exp_apigw_suggestion.test, exp_time_to_add_items.test_1, exp_checkout_tap4.test, exp_manage_subscription.control, exp_cl_omni_main.test, exp_comment_picker_and_courier.test, exp_newui_evaluate_order.test, exp_card_in_listing_v2.2_column, exp_is_sdk_binding_card_enabled.test, exp_feature_kpp_test.false, exp_nps_default_rate.rate_5, exp_search_suggestions_popular_sku.control, exp_default_payment_type.control, exp_personal_promo_swipe_animation.test, exp_loyalty_categories.test, exp_sdk_binding_card_enabled.test, exp_is_new_permissions_flow_enabled.true, exp_cl_omni_refusalprintcoupons.test, exp_newui_cart_cancel_editing.test, exp_cl_omni_action.test, exp_email_edit_enabled.true, exp_apigw_listing.test, exp_new_timing.test, exp_position_payment_type.test_C, exp_newui_authorization.test, exp_main_label_new.test, exp_feedback_pop_up_enabled.true, exp_use_loyalty_points.test, exp_cl_omni_support.test, exp_onboarding_editing_order.test, exp_cardOne_promo_type.test, exp_sdk_payment_enabled.test, exp_newui_cart_check_edit.control, exp_new_matrix.test, exp_general_editing_page.test, exp_omni_order_history.test, exp_closable_banner.test, exp_notification_on_main_page_close_button.true, exp_pickup_in_delivery.test, exp_newui_history.test, exp_newui_cart.test, exp_newui_cart_button.test, exp_editing_info.test, exp_delivery_price_info.test, exp_reviews_reasons.test, exp_sbp_enabled.test, exp_apigw_purchase.test, exp_cancel_subscription.test_2, exp_search_short_listing.25, exp_catalog_tag_navigation.test, exp_interval_jump.control, exp_popup_about_order.test, exp_is_new_filters_enabled.true, exp_is_reviews_enabled.true, exp_accrual_history.test, exp_loader_cart.bottom, exp_new_my_goods.test, exp_cl_new_splash.control, exp_welcome_onboarding.control, exp_edit_info.control, exp_card_in_listing.old, exp_in_app_update.test, exp_assembly_cost_location.cart, exp_cl_omni_authorization.test, exp_checkout_cart_promocode.test, exp_newui_history_active_action.test_stars, exp_newui_chips.test, exp_unlimit_recommendations.test, exp_notification_on_main_page.test, exp_success_page_banner.test, exp_start_page.test, exp_new_price_cart.test, exp_apigw_product_page.test, exp_apigw_catalog.test, exp_personal_recommendations.test_B, exp_catalog_alreadybought.test, exp_pdp_ds_recommendation.test, exp_local_sorting.true, exp_personal_promo_navigation.test, exp_search_sort_enabled.true, exp_new_notifications_show_unauthorized.test, exp_feedback_chat_enabled.false, exp_ct_banners.test, exp_growthbooks_aa.test, exp_editing_through_cancel.test, exp_omni_price.test, exp_click_collect.test, exp_is_sdk_payment_enabled.test, exp_apigw_recommendations.test, exp_default_replacement_method.control, exp_search_local_popularity.test, exp_suggestion_categories.test, exp_web_feature_test.true, exp_profile_login.false, exp_birthday_coupon_skus.test, exp_cl_omni_refusalprintreceipts.test, exp_profile_stories.test, exp_reset_sorting_type.test, exp_omni_cart.test, exp_mission_mvp.test, exp_profile_bell.test, exp_newui_cart_delivery.control, exp_pdp_ds_alsobuy.test, exp_total_price.test_2_down, exp_apigw_favorite.test, exp_hide_sorting_type_discount.false',
}


class LentaAPI:
    _url = 'https://api.lenta.com/v1/catalog/items'
    _headers = headers
    _payload = dto.ApiRequestPayload(
        categoryId=1028,
        sort={'type': 'popular', 'order': 'desc',},
        offset=0,
        limit=150
    )

    @classmethod
    def _fetch_items(cls) -> dto.ApiResponse:
        response = requests.post(cls._url, headers=cls._headers, json=cls._payload.model_dump(), verify=True)
        return dto.ApiResponse(**response.json())

    @classmethod
    def fetch_all_items(cls) -> list[dto.Item]:
        response = cls._fetch_items()
        items = response.items

        while response.total > cls._payload.offset + cls._payload.limit:
            cls._payload.offset += cls._payload.limit
            response = cls._fetch_items()
            items.extend(response.items)

        return items


items = LentaAPI.fetch_all_items()

with open('items.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'Название', 'Цена', 'Цена без скидки'])
    writer.writerows([(item.id, item.name, item.prices.price, item.prices.priceRegular) for item in items])
