const cart = {
    namespaced: true,
    state: {
        items: []
    },
    getters: {
        itemById: state => id => {
            return state.items.find(i => i.product === id)
        },
        checkById: state => id => {
            return (state.items.findIndex(i => i.product === id) === -1) ? false : true
        },
        amount: state => {
            return state.items.reduce((a, b) => +a + +b.amount, 0)
        },
        getItems: state => {
            return state.items
        }
    },
    mutations: {
        ADD_ITEM (state, product) {
            state.items.push({
                name: product.name,
                product: product.id,
                quantity: 1,
                price: product.price,
                amount: +product.price,
                image: product.small_img
            })
        },
        INCREMENT_QUANTITY (state, id) {
            let item = state.items.find(i => i.product === id)
            if (item.quantity === 30) return
            ++item.quantity
            item.amount = item.price * item.quantity
        },
        DECREMENT_QUANTITY (state, id) {
            let item = state.items.find(i => i.product === id)
            if (item.quantity === 1) return
            --item.quantity
            item.amount = item.price * item.quantity
        },
        SET_CART (state, cart) {
            state.items = cart
        }
    },
    actions: {
        async loadCart ({ commit }) {
            let { data } = await this._vm.$axios.get('/menu/init-cart/')
            commit('SET_CART', data.cart)
        },
        async saveCart ({ state }) {
            await this._vm.$axios.post('/menu/init-cart/', state.items)
        },
        increment ({ commit, dispatch }, id) {
            commit('INCREMENT_QUANTITY', id)
            dispatch('saveCart')
        },
        decrement ({ commit, dispatch }, id) {
            commit('DECREMENT_QUANTITY', id)
            dispatch('saveCart')
        },
        addItemToCart ({ commit, dispatch }, product) {
            commit('ADD_ITEM', product)
            dispatch('saveCart')
        }
    }
}

export default cart