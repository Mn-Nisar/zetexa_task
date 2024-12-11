CREATE TABLE user(
user_id INTEGER PRIMARY,
name VARCHAR(255),
email VARCHAR(255)
)

CREATE TABLE posts(
post_id INTEGER PRIMARY,
user_id INTEGER FOREIGN KEY (user_id) REFERENCES users
title VARCHAR(255),
content VARCHAR(255),
cretated_at DATETIME,
)

CREATE TABLE comments(
comment_id INTEGER PRIMARY,
post_id INTEGER FOREIGN KEY (post_id) REFERENCES posts,
user_id INTEGER FOREIGN KEY (user_id) REFERENCES users,
comment_text VARCHAR(255),
created_at DATETIME,
)

-- 1
SELECT 
    posts.post_id, 
    posts.content, 
    COUNT(comments.comment_id) AS comment_count
FROM posts
LEFT JOIN comments ON posts.post_id = comments.post_id
GROUP BY posts.post_id, posts.content
ORDER BY posts.created_at DESC
LIMIT 5;

--2
SELECT users.user_id, users.name
FROM users
LEFT JOIN posts ON users.user_id = posts.user_id
WHERE posts.post_id IS NULL;




