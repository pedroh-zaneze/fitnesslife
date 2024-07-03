// Dados de exemplo para alimentação
const alimentacao = {
    "2024-06-28": {
        "carb_consumidos": 100,
        "prot_consumidas": 50,
        "gord_consumidas": 25,
        "kcal_consumidas": 1000,
        "carb_meta": 200,
        "prot_meta": 100,
        "gord_meta": 50,
        "kcal_meta": 1500,
        "refeicoes": {
            "Café da Manhã": [{ "alimento": "Ovos Mexidos", "carboidratos": 10, "proteinas": 20, "gorduras": 15, "kcal": 250 }],
            "Almoço": [{ "alimento": "Arroz", "carboidratos": 40, "proteinas": 5, "gorduras": 2, "kcal": 200 }],
            "Jantar": [],
            "Lanches": [{ "alimento": "Maçã", "carboidratos": 15, "proteinas": 0, "gorduras": 0, "kcal": 60 }]
        }
    }
};

// Dias da semana
const week_days = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"];

// Carregar os dados da alimentação para o dia atual
const today = new Date();
const options = { weekday: 'long', day: 'numeric', month: 'long' };
const todayDateFormat = today.toLocaleDateString('pt-BR', options);
document.getElementById('currentDate').textContent = todayDateFormat;
const todayISOString = today.toISOString().slice(0, 10);
loadAlimentacao(todayISOString);

// Função para carregar os dados da alimentação para uma data específica
function loadAlimentacao(date) {
    const data = alimentacao[date];

    // Atualizar o título com a data atual
    document.getElementById('currentDate').textContent = date;

    // Atualizar os valores de consumo de nutrientes
    document.getElementById('carb_consumidos').textContent = data.carb_consumidos;
    document.getElementById('prot_consumidas').textContent = data.prot_consumidas;
    document.getElementById('gord_consumidas').textContent = data.gord_consumidas;
    document.getElementById('kcal_consumidas').textContent = data.kcal_consumidas;

    // Atualizar as metas de consumo de nutrientes
    document.getElementById('carb_meta').textContent = data.carb_meta;
    document.getElementById('prot_meta').textContent = data.prot_meta;
    document.getElementById('gord_meta').textContent = data.gord_meta;
    document.getElementById('kcal_meta').textContent = data.kcal_meta;

    // Atualizar a barra de progresso de calorias
    const progress = (data.kcal_consumidas / data.kcal_meta) * 100;
    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = `${progress}%`;

    // Atualizar a cor da barra de progresso
    if (progress >= 100) {
        progressBar.classList.remove('bg-info');
        progressBar.classList.remove('bg-danger');
        progressBar.classList.add('bg-success');
    } else if (progress <= 50) {
        progressBar.classList.remove('bg-success');
        progressBar.classList.remove('bg-info');
        progressBar.classList.add('bg-danger');
    } else {
        progressBar.classList.remove('bg-success');
        progressBar.classList.remove('bg-danger');
        progressBar.classList.add('bg-info');
    }

    // Limpar as listas de refeições
    const refeicoes = ["Café da Manhã", "Almoço", "Jantar", "Lanches"];
    refeicoes.forEach(refeicao => {
        const lista = document.getElementById(`refeicao_${refeicao.toLowerCase().replace(" ", "_")}`);
        lista.innerHTML = '';
        data.refeicoes[refeicao].forEach(item => {
            lista.innerHTML += `<li>${item.alimento} - Carb: ${item.carboidratos}g, Prot: ${item.proteinas}g, Gord: ${item.gorduras}g, Kcal: ${item.kcal}</li>`;
        });
    });
}

// Função para carregar os dados da alimentação para o dia selecionado
function loadDay(direction) {
    const currentDateElement = document.getElementById('currentDate');
    const currentDate = new Date(currentDateElement.innerText);

    let newDate;
    if (direction === 'previous') {
        newDate = new Date(currentDate);
        newDate.setDate(currentDate.getDate() - 1);
    } else {
        newDate = new Date(currentDate);
        newDate.setDate(currentDate.getDate() + 1);
    }

    const options = { weekday: 'long', day: 'numeric', month: 'long' };
    const newDateFormat = newDate.toLocaleDateString('pt-BR', options);
    currentDateElement.textContent = newDateFormat;

    const newDateString = newDate.toISOString().slice(0, 10);
    loadAlimentacao(newDateString);
}

// Função para adicionar um alimento a uma refeição
function adicionarRefeicao(refeicao) {
    const alimento = prompt("Digite o nome do alimento:");
    const carboidratos = parseFloat(prompt("Digite a quantidade de carboidratos (em gramas):"));
    const proteinas = parseFloat(prompt("Digite a quantidade de proteínas (em gramas):"));
    const gorduras = parseFloat(prompt("Digite a quantidade de gorduras (em gramas):"));
    const kcal = parseFloat(prompt("Digite a quantidade de calorias (em kcal):"));

    if (!alimento || isNaN(carboidratos) || isNaN(proteinas) || isNaN(gorduras) || isNaN(kcal)) {
        alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    // Coloque aqui a lógica para adicionar o alimento ao banco de dados
    // Substitua este exemplo pela lógica real
    const today = document.getElementById('currentDate').innerText;
    if (!alimentacao[today]) {
        alimentacao[today] = {
            "carb_consumidos": 0,
            "prot_consumidas": 0,
            "gord_consumidas": 0,
            "kcal_consumidas": 0,
            "carb_meta": 0,
            "prot_meta": 0,
            "gord_meta": 0,
            "kcal_meta": 0,
            "refeicoes": {
                "Café da Manhã": [],
                "Almoço": [],
                "Jantar": [],
                "Lanches": []
            }
        };
    }

    alimentacao[today].carb_consumidos += carboidratos;
    alimentacao[today].prot_consumidas += proteinas;
    alimentacao[today].gord_consumidas += gorduras;
    alimentacao[today].kcal_consumidas += kcal;

    alimentacao[today].refeicoes[refeicao].push({ "alimento": alimento, "carboidratos": carboidratos, "proteinas": proteinas, "gorduras": gorduras, "kcal": kcal });

    loadAlimentacao(today);
}
