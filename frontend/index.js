$(document).ready(function() {
    $('#load-films').click(function() {
        $.post('/load_films', function() {
            loadFilms();
        });
    });

    function loadFilms() {
        $.get('/films', function(data) {
            const films = data.films;
            const tbody = $('#films-table tbody');
            tbody.empty();
            films.forEach(film => {
                tbody.append(`<tr>
                    <td>${film.name}</td>
                    <td>${film.description}</td>
                    <td>${film.rating}</td>
                </tr>`);
            });
        });
    }

    // Загрузка фильмов при загрузке страницы
    loadFilms();
});
