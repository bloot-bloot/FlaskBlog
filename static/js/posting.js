
$(document).ready( ()=> {
    let form = $("#posting");
    load_posts();
    console.log(form);
    form.submit( (event) => {
        // е - событие
        // submit - регистрирует обработчик события == (addeventListner)
        event.preventDefault();

        let post = $("textarea[name='post_text']")
        let id = $("input[name=id]")
        if (post.val() == ""){
            return;
        } 
        let post_data = {
            id: id.val(),
            post_text: post.val()
            // post_dat = обьект с данныеми из формы 
            // формируем потому что ajax принимает только обьект
            
        }
        
        $.ajax({
            method:"POST",
            url:"/posts", 
            data: post_data

        }).done((resp) => {

            console.log(resp);
        
            let result = resp["result"][0];
            console.log(result);
            let post = new Post (result.display_name, result.text, result.date);
            let post_cont = document.querySelector('#posts');
            add_post(post_cont, post.ganerate());

        })
        // done обработчик событий который говорит что все ок 
        console.log(post.val(), id.val());

    }
    )
})
/*
<div class="container-post lead">
    <div class = "user text-primary">{{ name }}</div>
    <div class = "post text-primary bg-info">{{post["text"]}}</div>
    <div class = "time text-muted small text-right">{{post["updated"]}}</div>
</div> 
*/

function Post (auther, text, data) {
    console.log(auther, text, data);
    this.auther = auther,
    this.text = text,
    this.data = data,
    this.ganerate = () => {
        let div_container = document.createElement('div');
        div_container.className = "container-post lead";
        // создаем шаблон 
        let user = document.createElement('div');
        let post = document.createElement('div');
        let time = document.createElement('div');

        user.className = "user";
        post.className = "post";
        time.className = "time";

        user.textContent = this.auther;
        post.textContent = this.text;
        time.textContent = this.data;

        div_container.appendChild(user);
        div_container.appendChild(post);
        div_container.appendChild(time);

        return div_container;
    }
}

function add_post (container, post) {
    container.prepend(post);
    // prepend - добавление в начало 
}
function load_posts(){
    var login = $("input[name=dp_name]").val()

    $.ajax({
        // ajax -запрос 
        method:"GET",
        url:"/posts/" + login
        // методы запроса 
    }).done((resp) =>{
        // resp наши данные от сервера 
        // done - ответ на 200
        console.log(resp);
        let post_cont = document.querySelector('#posts');

        resp.forEach(post => {
            console.log(post);
            let newPost = new Post (login, post.text, post.updated);
            //newPost  информация которую ввел пользователь (получение постов от БАЗЫ ДЫННЫХ)
            add_post(post_cont, newPost.ganerate());
            // добавляем новый пост в ленту 
        });
    })
}
