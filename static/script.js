$(document).ready(function() {
    // Criar filtros individuais para cada coluna
    $('#tabela-dados thead th').each(function() {
        const title = $(this).text();
        $('#filtrosColunas').append(`
            <div class="col-md-3 filtro-coluna">
                <input type="text" class="form-control filtro-coluna-input" 
                       placeholder="Filtrar ${title}" 
                       data-column="${$('#tabela-dados thead th').index($(this))}">
            </div>
        `);
    });

    // Função de filtro geral
    $('#pesquisaGeral').on('keyup', function() {
        const value = $(this).val().toLowerCase();
        $('#tabela-dados tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    // Função de filtro por coluna
    $('.filtro-coluna-input').on('keyup', function() {
        const column = $(this).data('column');
        const value = $(this).val().toLowerCase();

        $('#tabela-dados tbody tr').each(function() {
            const cell = $(this).find('td').eq(column).text().toLowerCase();
            $(this).toggle(cell.indexOf(value) > -1);
        });
    });

    // Ordenação por coluna
    $('#tabela-dados thead th').click(function() {
        const table = $(this).parents('table').eq(0);
        const rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()));
        this.asc = !this.asc;
        if (!this.asc) rows = rows.reverse();
        table.children('tbody').empty().append(rows);
    });

    function comparer(index) {
        return function(a, b) {
            const valA = $(a).children('td').eq(index).text().replace(',', '');
            const valB = $(b).children('td').eq(index).text().replace(',', '');
            return $.isNumeric(valA) && $.isNumeric(valB) ?
                valA - valB : valA.localeCompare(valB);
        };
    }
});