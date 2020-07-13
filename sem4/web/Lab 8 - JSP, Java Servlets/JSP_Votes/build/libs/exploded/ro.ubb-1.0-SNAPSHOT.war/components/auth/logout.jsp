<%

    session.removeAttribute("user_session");


    session.setAttribute("login_message", "Sign out Successfull");


%>

<script type="text/javascript">
    window.location.href="/components/auth/login.jsp";
</script>
