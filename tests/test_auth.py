import pytest
from playwright.sync_api import expect

def test_login_page_loads(page):
    """Test that login page loads correctly"""
    page.goto("https://rahulshah22.pythonanywhere.com/login") 
    
def test_login_with_valid_credentials(page):
    """Test login with valid credentials"""
    page.goto("https://rahulshah22.pythonanywhere.com/login") 
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    expect(page).to_have_url("https://rahulshah22.pythonanywhere.com/")

def test_login_with_invalid_credentials(page):
    """Test login with invalid credentials"""
    page.goto("https://rahulshah22.pythonanywhere.com/login") 
    page.fill("input[name='username']", "invalid_username")
    page.fill("input[name='password']", "invalid_password")
    page.click("button[type='submit']")
    expect(page).to_have_url("https://rahulshah22.pythonanywhere.com/login/")

def test_logout(page):
    """Test logout functionality"""
    pass