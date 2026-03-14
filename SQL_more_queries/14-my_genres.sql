-- lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
```

---

### 📖 Explanation

This time we need data from **3 tables** at once, so we use **two JOINs chained together**!

Think of it like a chain:
```
tv_genres → tv_show_genres → tv_shows
