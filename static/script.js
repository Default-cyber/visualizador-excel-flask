$(document).ready(function() {
    const table = $('#tabela-dados').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'print'
        ],
        language: {
            url: '//cdn.datatables.net/plug-ins/2.0.7/i18n/pt-BR.json'
        },
        responsive: true,
        pageLength: 25,
        order: [[0, 'asc']],
        initComplete: function() {
            // Cria filtros para cada coluna
            this.api().columns().every(function(index) {
                const column = this;
                const title = $(column.header()).text();
                const filterId = `filtro-col-${index}`;

                // Cria container do filtro
                $('#filtros-rapidos').append(`
                    <div class="col-md-3 mb-2">
                        <select id="${filterId}" class="form-select filtro-coluna" multiple="multiple" 
                                data-placeholder="Filtrar ${title}" style="width: 100%">
                        </select>
                    </div>
                `);

                // Preenche opções
                column.data().unique().sort().each(function(value) {
                    $(`#${filterId}`).append(
                        `<option value="${value}">${value}</option>`
                    );
                });

                // Inicializa Select2
                $(`#${filterId}`).select2({
                    allowClear: true,
                    placeholder: $(this).data('placeholder')
                });

                // Aplica filtro
                $(`#${filterId}`).on('change', function() {
                    const values = $(this).val();
                    column.search(values ? values.join('|') : '', true, false).draw();
                });
            });
        }
    });

    // Botão de reset
    $('#filtros-rapidos').append(`
        <div class="col-md-3 mb-2 d-flex align-items-center">
            <button class="btn btn-danger w-100" id="reset-filtros">
                <i class="bi bi-x-circle"></i> Limpar Filtros
            </button>
        </div>
    `);

    $('#reset-filtros').click(function() {
        $('.filtro-coluna').val(null).trigger('change');
        table.search('').columns().search('').draw();
    });
});