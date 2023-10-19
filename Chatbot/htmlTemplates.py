css = '''
<style>
.chat-message{
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom:1rm; 
    display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
    width: 15%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;;
    object-fit: cover;
}
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
}
'''
# </style>




bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/qWBwpNb/Photo-logo-5.png">
    </div>
    <div class="message"> {{MSG}}</div>
    
</div>

'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://instagram.fdel27-3.fna.fbcdn.net/v/t51.2885-19/294511699_2287272051424856_7153891157088429072_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdel27-3.fna.fbcdn.net&_nc_cat=108&_nc_ohc=XbeguOSuDJUAX_6ejwu&edm=ACWDqb8BAAAA&ccb=7-5&oh=00_AfB2VbYI7agdHQR88yWt6_nZPFP5HwMQVJGH7JToEAiUAw&oe=651C37F1&_nc_sid=ee9879">
    </div>
    <div class="message"> {{MSG}}</div>
</div>

'''
