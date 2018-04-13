# Try Django 1.11

<p>
    The project is based on <a href="https://www.youtube.com/watch?v=yDv5FIAeyoY">Try Django 1.11</a> tutorial by CodingEntrepreneurs.
    <br/>Hosted on <a href="https://gabriel-muy-picky.herokuapp.com/">heroku</a>.
</p>

Things that have been modified after finishing the tutorial:
<ul>
    <li>added bootstrap</li>
    <li>modified relation restaurant-user
        <ul>
            <li>any authenticated user can see and add items to any restaurant</li>
            <li>anonymous users can see the restaurants list</li>
            <li>anonymous users can see a general user-feed</li>
            <li>modified query (search) to show the right values</li>
        </ul>
    <li>Added: menu bar: option to see all restaurants</li>
    <li>Added: auto add restaurant to user's list when adding/modifying an item</li>
    <li>Added: option to see all users</li>
    <li>Added: email confirmation for new accounts</li>
    <li>Added: option to modify the username or the password</li>
    <li>Added: dj-static and django-toolbelt to render properly the admin page on heroku</li>
    <li>Added: Password reset</li>

</ul>
