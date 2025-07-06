import streamlit as st
import re
import dns.resolver
from validate_email_address import validate_email

# -------------------------------
# Utility functions
# -------------------------------

# 1. Check email format
def is_valid_format(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# 2. Check if domain exists
def domain_exists(email):
    try:
        domain = email.split('@')[-1]
        dns.resolver.resolve(domain, 'MX')
        return True
    except:
        return False

# 3. Check if email is disposable
def is_disposable(email):
    disposable_domains = ['mailinator.com', '10minutemail.com', 'tempmail.com']
    domain = email.split('@')[-1].lower()
    return domain in disposable_domains

# 4. SMTP check (optional but cool)
def smtp_check(email):
    try:
        return validate_email(email, verify=True)
    except:
        return False

# -------------------------------
# Streamlit UI
# -------------------------------

st.set_page_config(page_title="Mail ID Validator", page_icon="📧")
st.title("📧 Mail ID Validator")

email = st.text_input("Enter an email address to validate:")

if st.button("Validate"):
    if not email:
        st.warning("Please enter an email address.")
    elif not is_valid_format(email):
        st.error("❌ Invalid email format.")
    elif not domain_exists(email):
        st.error("❌ Email domain does not exist.")
    elif is_disposable(email):
        st.warning("⚠️ This appears to be a disposable email.")
    else:
        result = smtp_check(email)
        if result:
            st.success("✅ Email is valid and reachable.")
        else:
            st.info("ℹ️ Email format and domain are valid, but mailbox could not be verified (SMTP check failed or blocked).")

    # Show summary
    st.markdown("---")
    st.subheader("🔎 Summary:")
    st.write(f"**Email Entered:** {email}")
    st.write(f"**Valid Format:** {'✅' if is_valid_format(email) else '❌'}")
    st.write(f"**Domain Exists:** {'✅' if domain_exists(email) else '❌'}")
    st.write(f"**Disposable:** {'⚠️ Yes' if is_disposable(email) else '❌ No'}")
    st.write(f"**SMTP Check:** {'✅ Reachable' if smtp_check(email) else 'ℹ️ Not Verified'}")



st.markdown("<br><br><br>", unsafe_allow_html=True)
# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; padding-top: 10px;'>
        Developed with ❤️ by <strong>Dheeraj</strong> 
    """,
    unsafe_allow_html=True
)

