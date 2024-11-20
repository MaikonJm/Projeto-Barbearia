$(document).ready(function () {
    // Ao submeter o formulário, reseta os campos e envia os dados
    $('#registroForm').on('submit', function (event) {
        // Impede o envio do formulário para resetar os campos
        event.preventDefault();

        // Reseta os campos de seleção para o valor padrão
        $('#funcionario').prop('selectedIndex', 0); // Reseta para "Selecione"
        $('#servico').prop('selectedIndex', 0); // Reseta para "Selecione"
        
        // Envia o formulário após o reset dos campos
        this.submit();  // Envia para o backend
        console.log("Serviço registrado!");

        // Caso deseje adicionar algum feedback para o usuário, pode adicionar um alerta ou modal
    });

    // Função para carregar o conteúdo do histórico com base na página
    function loadHistorico(page) {
        $.ajax({
            url: '/?page=' + page,  // A URL com o número da página
            method: 'GET',
            success: function(response) {
                // Atualiza o conteúdo da tabela e os controles de paginação
                $('#historicoTabelaBody').html($(response).find('#historicoTabelaBody').html());
                $('#paginationControls').html($(response).find('#paginationControls').html());
            },
            error: function() {
                alert("Erro ao carregar o histórico!");
            }
        });
    }

    // Função para navegação entre as páginas
    window.navigatePage = function (page) {
        loadHistorico(page);
    };
});
