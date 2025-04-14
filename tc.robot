*** Settings ***
Documentation     Campaign Goal
Test Teardown     Browser.Close Browser
# Suite Setup       login_and_navigate_to_order    Deepintent    DeepIntent
# Suite Teardown    logout_and_close_browser
Force Tags        RFR     CAMPAIGN_UI
Library           Browser       auto_closing_level=MANUAL
Library           String
Library           ../../../ExternalLibrary/Common/Login.py
Library           ../../../ExternalLibrary/Common/Common.py
Library           ../../../ExternalLibrary/DSP/UI/Campaign/Campaign.py
Library           ../../../ExternalLibrary/DSP/UI/Campaign/CampaignCommon.py
Library           ../../../ExternalLibrary/DSP/UI/CampaignGroup/CampaignGroupListing.py
Library           ../../../ExternalLibrary/DSP/UI/Campaign/CampaignCreative.py
Library           ../../../ExternalLibrary/Common/DB.py
Library           ../../../ExternalLibrary/Common/CommonAPI.py
Library           ../../../../ExternalLibrary/DSP/API/Campaign/AuditLogs.py
Resource          Create.resource
Resource          ../SmartView/Create_data.resource
Library           pabot.PabotLib


*** Variables ***
${advertiserId}    10001
${org_name}    10000    # Deepintent
${adv_name}    10001     # DeepIntent

${adv_id}       10642
${org_id}       10137
*** Test Cases ***
01_Clone_Campaign_with_AMCO_ON
    [Tags]    AAA
    [Timeout]    20 minutes
    login_and_navigate_to_order    ${org_name}    ${adv_name}
    ${bidOptimizerEnabled}    Set Variable    1
    ${config}    Set Variable    {"amcoAlgoControl": "BALANCED"}
    ${billingUnit}    Set Variable    CPM
    ${uniqueReach}    Set Variable    OFF
    ${amco}    Set Variable    on
    ${campaign_general}    Order and Campaign Clone    ${advertiserId}    Video    CPCV    0.45    ${billingUnit}    ${uniqueReach}    ${amco}
    ${campaign_name}    Set Variable    ${campaign_general}[Campaign General][Campaign Name]
    ${campaign_id}    Set Variable    ${campaign_general}[Campaign Goal][Campaign ID]
    ${before_clone_data}=    DB.Execute Query    db_query=select bidOptimizerEnabled,uniqueReachEnabled,config from bidder.CAMPAIGN_OPTIMIZER where campaignId=${campaign_id};
    log    ${before_clone_data}
    should be equal as strings    ${before_clone_data}[0][0]    ${bidOptimizerEnabled}
    should be equal as strings    ${before_clone_data}[0][1]    0
    ${campaign_data_clone}    campaign_clone    ${campaign_general}
    ${campaign_id}    Set Variable    ${campaign_data_clone}[Campaign Goal][Campaign ID]
    ${after_clone_data}=    DB.Execute Query    db_query=select bidOptimizerEnabled,uniqueReachEnabled,config from bidder.CAMPAIGN_OPTIMIZER where campaignId=${campaign_id};
    should be equal as strings    ${after_clone_data}[0][0]    ${bidOptimizerEnabled}
    should be equal as strings    ${after_clone_data}[0][1]    0
    should be equal as strings    ${after_clone_data}[0][2]    ${config}
    campaign_summary
    logout
