import pytest
from playwright.sync_api import expect

def test_add_code_snippets_to_post(page):
    """Test adding a code snippet to a post"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.click("a[href='/post/14/']")
    page.click("a[href='/post/14/edit/']")
    page.click("button#add-snippet")
    page.fill('//*[@id="code-snippets"]/div[2]/div/div/div[1]/input', "Test Code Snippet")
    page.select_option('//*[@id="code-snippets"]/div[2]/div/div/div[2]/select', "python")
    page.fill('//*[@id="code-snippets"]/div[2]/div/div/div[3]/textarea', "print('Test Hello World!')")
    page.click("button[type='submit']")
    expect(page).to_have_url("http://127.0.0.1:8000/post/14/")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")

def test_edit_code_snippet(page):
    """Test editing an existing code snippet"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.click("a[href='/post/14/']")
    page.click("a[href='/post/14/edit/']")
    page.fill('//*[@id="code-snippets"]/div/div/div/div[1]/input', "Update Code Snippet")
    page.select_option('//*[@id="code-snippets"]/div/div/div/div[2]/select', "python")
    page.fill('//*[@id="code-snippets"]/div/div/div/div[3]/textarea', "print('Hello, World!')")
    expect(page.locator('//*[@id="code-snippets"]/div[1]/div/div/button')).to_have_text("Remove Snippet")
    page.click("button[type='submit']")
    expect(page).to_have_url("http://127.0.0.1:8000/post/14/")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")


def test_delete_code_snippet(page):
    """Test removing a code snippet from a post"""
    pass

def test_multiple_code_snippets(page):
    """Test adding multiple code snippets to a post"""
    page.goto("http://127.0.0.1:8000/login")
    page.fill("input[name='username']", "rahulshah")
    page.fill("input[name='password']", "Rshah22@22")
    page.click("button[type='submit']")
    page.click("a[href='/post/14/']")
    page.click("a[href='/post/14/edit/']")
    page.click("//button[@id='add-snippet']")
    page.click(f'//*[@id="code-snippets"]/div[3]/div/div/button')
    page.click("button[type='submit']")
    expect(page).to_have_url("http://127.0.0.1:8000/post/14/")
    page.click("a[href='/logout/']")
    expect(page).to_have_url("http://127.0.0.1:8000/")