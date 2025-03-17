import pytest
from playwright.sync_api import expect

def test_login_page_loads(page):
    """Test that login page loads correctly"""
    page.goto("http://127.0.0.1:8000/login") 
    
def test_login_with_valid_credentials(page):
    """Test login with valid credentials"""
    page.goto("http://127.0.0.1:8000/login") 
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

def test_login_with_invalid_credentials(page):
    """Test login with invalid credentials"""
    page.goto("http://127.0.0.1:8000/login") 
    page.fill("input[name='username']", "invalid_username")
    page.fill("input[name='password']", "invalid_password")
    page.click("button[type='submit']")
    expect(page).to_have_url("http://127.0.0.1:8000/login/")

def test_logout(page):
    """Test logout functionality"""
    pass