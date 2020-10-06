<template>
    <a :href="url" class="uk-navbar-item ss-basket">
        <div class="uk-visible@m uk-margin-small-right">
            <span v-if="amount == 0">Корзина</span>
            <span v-else>{{amount}} ₽</span>
        </div>
        <img src="/static/shop/basket.svg" uk-svg width="20" height="20">
    </a>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex';

    export default {
        name: 'basket',
        props: ['url'],
        mounted () {
            this.loadCart()
        },
        computed: {
            ...mapGetters({
                amount: 'cart/amount'
            })
        },
        methods: {
            ...mapActions({
                loadCart: 'cart/loadCart'
            })
        }
    }
</script>

<style scoped>

</style>