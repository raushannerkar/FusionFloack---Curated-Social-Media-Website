document.addEventListener("DOMContentLoaded", function() {
    const likeButtons = document.querySelectorAll(".like-btn");

    likeButtons.forEach(button => {
        button.addEventListener("click", function() {
            const postId = this.getAttribute("data-post-id");
            const url = `/like/${postId}/`;

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const likeCountSpan = button.nextElementSibling;
                    likeCountSpan.textContent = data.likes_count;

                    // Toggle 'liked' class based on user authentication and like status
                    if (data.liked) {
                        button.classList.add("liked");
                    } else {
                        button.classList.remove("liked");
                    }
                });
        });
    });
});
