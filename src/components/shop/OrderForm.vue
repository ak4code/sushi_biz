<template>
    <div class="order-form">
        <form class="uk-form-stacked" @submit.prevent="submitOrder">
            <div class="uk-margin">
                <label class="uk-form-label" for="name">Имя</label>
                <div class="uk-form-controls">
                    <input class="uk-input uk-border-rounded" required id="name" type="text" placeholder="Имя"
                           v-model="order.name">
                </div>
            </div>
            <div class="uk-margin">
                <label class="uk-form-label" for="phone">Телефон +7 ___ ___-__-__</label>
                <div class="uk-form-controls">
                    <input class="uk-input uk-border-rounded" required id="phone" type="text"
                           placeholder="+7 ___ ___-__-__" v-model="order.phone">
                </div>
            </div>
            <div class="uk-margin uk-flex uk-flex-wrap uk-child-width-1-1">
                <label class="uk-form-label">Способ доставки</label>
                <label class="ss-radio-button">
                    <input class="uk-radio" type="radio" name="delivery" :value="true" v-model="order.delivery">
                    Доставка
                </label>
                <label class="ss-radio-button">
                    <input class="uk-radio" type="radio" name="delivery" :value="false" v-model="order.delivery">
                    Самовывоз
                </label>
            </div>
            <div class="uk-margin" v-if="order.delivery">
                <label class="uk-form-label" for="address">Адрес</label>
                <div class="uk-form-controls">
                    <input class="uk-input uk-border-rounded" required v-model="order.address" id="address"
                           type="text"
                           placeholder="Темрюк, ул. Таманская 6">
                </div>
            </div>
            <div class="uk-margin">
                <label class="uk-form-label" for="person">Количество персон</label>
                <div class="uk-form-controls">
                    <select class="uk-select uk-border-rounded" id="person" v-model="order.person">
                        <option v-for="n in 10" :key="n">{{n}}</option>
                    </select>
                </div>
            </div>
            <div class="uk-margin">
                <div class="uk-form-controls">
                    <button class="uk-button uk-border-rounded uk-button-primary uk-width-1-1">
                        ОФОРМИТЬ ЗАКАЗ
                    </button>
                </div>
            </div>
            <div class="uk-margin uk-text-muted">
                <small>
                    Нажимая кнопку «Оформить заказ», я подтверждаю свою дееспособность,
                    согласие на обработку персональных
                    данных в соответствии с указанным <a href="/policy/" target="_blank">здесь</a>
                    текстом.
                </small>
            </div>
        </form>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex'

    export default {
        name: 'order-form',
        data: () => ({
            order: {
                name: '',
                phone: '',
                address: '',
                person: 1,
                delivery: true,
            },
        }),
        computed: {
            ...mapGetters({
                items: 'cart/getItems',
            })
        },
        methods: {
            async submitOrder () {
                await this.$axios.post('/api/orders', { ...this.order, items: this.items })
                    .catch(err => console.log(err))
            }
        }
    }
</script>

<style scoped>

</style>