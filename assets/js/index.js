const Home = {template: '<h1>This is a home page</h1>'};
const Conversations = {template: '<h1>This is an all conversations page</h1>'};
const Unread = {template: '<h1>This is a unread messages page</h1>'};
const NewMessage = {template: '<h1>This is a new message page</h1>'};
const Login = {template: '#tpl-login'};
const routes = [
    {path: '/', component: Home},
    {path: '/conversations', component: Conversations},
    {path: '/unread', component: Unread},
    {path: '/newMessage', component: NewMessage},
    {path: '/login', component: Login}

];
const router = new VueRouter({
    routes
});
router.mode = 'html5';

const app = new Vue({router}).$mount('#app');


function logIn() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    this.$http.post("http://edi.iem.pw.edu.pl/bach/mail/api/login", {
        login: username,
        password: password
    }).then((response) => {
        console.log(response.status);
    });
}

