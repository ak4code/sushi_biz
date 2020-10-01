<template>
    <div class="ss-cart-item-list">
        <div class="ss-cart-item uk-flex uk-flex-wrap uk-flex-middle uk-grid-small" v-for="(item, index) in items"
             :key="item.product">
            <div class="item-image uk-width-auto">
                <div class="uk-cover-container">
                    <canvas width="100" height="100"></canvas>
                    <img :src="item.image" :alt="item.name" uk-cover>
                </div>
            </div>
            <div class="item-info uk-width-expand">
                <div class="uk-flex uk-flex-wrap uk-grid-small">
                    <div class="uk-width-expand">
                        <h5 class="uk-margin-small-bottom">{{item.name}}</h5>
                    </div>
                    <div class="uk-width-1-5@m uk-text-center">
                        <div class="uk-inline">
                            <a class="uk-form-icon" uk-icon="icon: minus" @click.prevent="decrement(item.product)"></a>
                            <input class="uk-input uk-form-small uk-text-center" readonly style="padding-right: 40px"
                                   type="text" :value="itemCart(item.product).quantity">
                            <a class="uk-form-icon uk-form-icon-flip" uk-icon="icon: plus"
                               @click.prevent="increment(item.product)"></a>
                        </div>
                        <small>{{item.price}} ₽ / шт.</small>
                    </div>
                    <div class="uk-width-1-5@m uk-flex-first uk-text-center uk-flex-last@m">
                        <div class="uk-text-large uk-text-bold">
                            {{item.amount}} ₽
                        </div>
                    </div>
                </div>
            </div>
            <div class="uk-width-auto uk-padding-small">
                <a @click="removeItemFromCart(index)" uk-icon="trash"></a>
            </div>
        </div>
        <div class="uk-width-1-1 uk-padding-small uk-text-right">
            <div class="uk-text-large uk-text-bolder">Итого: {{amount}} ₽</div>
            <small class="uk-text-muted">* Без учета стоимости доставки</small>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex'

    export default {
        name: 'cart-item-list',
        computed: {
            ...mapGetters({
                items: 'cart/getItems',
                checkInCart: 'cart/checkById',
                itemCart: 'cart/itemById',
                amount: 'cart/amount'
            })
        },
        methods: {
            ...mapActions('cart', [
                'increment',
                'decrement',
                'removeItemFromCart'
            ])
        }
    }
</script>

<style scoped>

</style>