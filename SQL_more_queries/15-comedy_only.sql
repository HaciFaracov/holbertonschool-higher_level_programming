-- lists all Comedy shows in hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
```

---

### 📖 Explanation

This is basically the **opposite of task 14**! Last time we had a show and wanted its genres, now we have a genre and want its shows.

The chain is the same 3 tables but we filter differently:
```
tv_shows → tv_show_genres → tv_genres
