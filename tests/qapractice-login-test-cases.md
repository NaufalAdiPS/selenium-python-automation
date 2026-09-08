# Login — Test Cases & Expected Behaviors

Source: QA Practice (https://www.qapractice.com) — free QA automation practice.

## TC01: Valid login

Steps:
  1. Enter user@premiumbank.com in the email field
  2. Enter Bank@123 in the password field
  3. Click Sign in

Expected: A success message "Login Successful! Welcome to Premium Banking." is shown.

## TC02: Both fields empty

Steps:
  1. Leave email and password empty
  2. Click Sign in

Expected: Error "Email and Password are required" is shown.

## TC03: Missing password

Steps:
  1. Enter a valid email
  2. Leave password empty
  3. Click Sign in

Expected: Error "Password is required" is shown.

## TC04: Missing email

Steps:
  1. Leave email empty
  2. Enter any password
  3. Click Sign in

Expected: Error "Email is required" is shown.

## TC05: Invalid credentials

Steps:
  1. Enter wrong@example.com
  2. Enter a wrong password
  3. Click Sign in

Expected: Error "Invalid email id and password" is shown; no success message.

## TC06: Password is masked

Steps:
  1. Type any value into the password field

Expected: The characters are obscured (input type="password").

## TC07: Forgot-password navigation

Steps:
  1. Click the "Forgot password?" link

Expected: The browser navigates to /forget-password.

## TC08: Register navigation

Steps:
  1. Click the "Register now" link

Expected: The browser navigates to /register.
