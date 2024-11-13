const BASE_URL = 'https://api.exemplo.com';

// Função para buscar dados iniciais do contador
export async function fetchCounterData() {
    try {
        const response = await fetch(`${BASE_URL}/counter/initial`);
        if (!response.ok) throw new Error('Erro ao buscar dados do contador');
        return await response.json();
    } catch (error) {
        console.error('Erro:', error);
        throw error;
    }
}

// Função para incrementar o contador na API
export async function incrementCounterData() {
    try {
        const response = await fetch(`${BASE_URL}/counter/increment`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        });
        if (!response.ok) throw new Error('Erro ao incrementar o contador');
        return await response.json();
    } catch (error) {
        console.error('Erro:', error);
        throw error;
    }
}
