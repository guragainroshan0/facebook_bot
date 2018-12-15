
<h1>facebook_bot</h1> 
<p>This is a file which has function for automating facebooks tasks. Only a few functions has been added. Selenium has been used to automate the tasks.</p>
  <h2>
  Dependencies</h2>
  <a href="https://www.seleniumhq.org"><p>Selenium</p></a>
  <h2>
  Functions</h2>
  <h3>
  login_to_facebook()</h3>
  <p>This will be automatically called when calling the constructor</p>
  <h3>
  get_friend_list(name,ids)
  </h3>
  <p>This function creates a file which contains the friend list of a user whose facebook username is "ids".
  The argument name is the filename and ids is the facebook username</p>
  <h3>
  myfriends()</h3>
  <p>This is the implementataion of get_friend_list() function where own username is passed</p>
  <h3>
  send_message(username,message,spam)
   </h3>
   <p> Username is the facebook username of the friend who is to be messaged
  message is the text to be messaged
  spam(optional boolean) spams the  username with message by default spam is false
  </p>
  <h3>
  message_all(message)
  </h3>
  <p>sends messages to all the friends in the friend list, "message" is the text to be sent</p>
  <h3>
  like(username)
  </h3>
  <p>Username(optional string). By default it is None. This function likes all the posts in the news feed of a the user.
  if username of a friend is specified it likes all the posts in the timeline of the specified username
  </p>
  
