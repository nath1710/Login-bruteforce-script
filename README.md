# Brute force attack with python


<p align="center">
<a href="https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses">Lab: Username enumeration via different responses</a>
<p align="center">
  <a href="https://www.youtube.com/watch?v=DEUCRYGt3TY">
    <img src="https://img.youtube.com/vi/DEUCRYGt3TY/hqdefault.jpg" alt="Brute Force Attack with Python">
  </a>
</p>
</p>


### Exercise performed:
- In order to make the python script to execute a brute force attack, we started by understanding and solving the portswigger lab.

1. installed and run Burpsuite:

   https://portswigger.net/burp/communitydownload
   
2. Installing foxy proxy in firefox browser:

   https://addons.mozilla.org/es/firefox/addon/foxyproxy-standard/

3. Foxy proxy and burpsuite configuration is performed

### Laboratory resolution
I ran Burp and sent invalid credentials on the login page. In **Proxy > HTTP history, I located the POST /login request**, highlighted the username parameter and sent it to Burp Intruder. 
I set up a Sniper attack with a list of usernames and, by comparing the length of the server responses, identified the correct user. Then, 
I set the password parameter to load and repeated the process with a list of passwords, detecting the correct one in the same way. Finally, 
I logged in with the obtained credentials and accessed the account to complete the lab.

### Code design
To design the script, I based myself on the methodology used to solve the lab. I implemented the reading of .txt files containing the users and passwords, generating the POST request, whose code fragment is noted in the comments.
I had the code iterate over the contents of the files, obtaining the length of the server response. First, I tested the usernames and detected the correct one by finding a response with a different length. Then, I repeated the process 
with the passwords. Finally, I ran the script in the VS Code terminal with `python script.py` to verify its operation.

💡Note: This taking into account that for the exercise I would have a computer with only Python installed.;

✎ Note: If you want to leave me a comment or suggestion feel free to make a pull request to my code with the suggested changes or comments.
