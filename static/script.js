$(document).ready(function() {
    $('#tabela-dados').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'print'
        ],
        language: {
            url: '//cdn.datatables.net/plug-ins/2.0.7/i18n/pt-BR.json'
        },
        responsive: true,
        pageLength: 25,
        order: [[0, 'asc']]
    });
});