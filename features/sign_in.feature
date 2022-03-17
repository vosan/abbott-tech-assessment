Feature: Sign In

  Scenario: Verify sign in flow with 2-factor authentication
    Given Choose country and language page is opened
    When I submit country and language
    Then I should be on the Landing Page
    When I sign in with correct credentials
    Then I should be on the Identity Verification page
    When I click Submit button
    Then Verification code field should be displayed
    And Verify submit button is disabled
    When I enter verification code
    Then Verify submit button is enabled
    When I click Submit button
    Then I should be on the Upload Device page
