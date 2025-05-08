<div class="masthead">
    <div class="container">
        <div class="row g-0">
            <div class="col-md-6 masthead-text">
                <!--  template logic did not yet exist to display the uploaded image-->
                {% if "placeholder" in post.featured_image.url %}
                <img src="{% static 'images/giftboxgold.jpg' %}" width="20%" class="scale" alt="placeholder image" style="margin-bottom: 20px;">
                {% else %}
                <img src="{{ post.featured_image.url }}" width="20%" class="scale" alt="{{ post.title }}" style="margin-bottom: 20px;">
                {% endif %}
                <!-- Post title goes in these h1 tags -->
                <h1 class="post-title">{{ post.title }}</h1>
                <!-- Post author goes before the | the post's created date goes after -->
                <p class="post-subtitle">{{ post.author }} | {{ post.created_on }}</p>
            </div>
        </div>
    </div>
</div>
