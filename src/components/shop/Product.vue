<template>
    <div class="ss-product uk-margin-bottom">
        <div class="uk-card uk-card-default uk-card-small uk-text-center uk-border-rounded uk-overflow-auto uk-position-relative">
            <div class="uk-card-media-top uk-cover-container uk-position-relative">
                <canvas height="250"></canvas>
                <img :src="product.medium_img" :alt="product.name" uk-cover>
                <div class="uk-position-top-right ss-product-label">
                    {{product.label}}
                </div>
            </div>
            <div class="uk-card-body">
                <h3 class="uk-h5 ss-product-name uk-margin-remove">{{product.name}}</h3>
                <small v-html="product.short_text"></small>
                <div style="min-height: 59px">
                </div>
                <div class="uk-position-bottom uk-text-small" style="padding: 10px 5px">
                    <div class="uk-flex uk-flex-middle uk-flex-wrap uk-child-width-1-2@m uk-child-width-1-1">
                        <div class="uk-width-1-1 uk-margin-small" v-if="product.options.length">
                            <select class="uk-select uk-form-small" name="modificator" id="modificator"
                                    v-model="modificator">
                                <option :value="option.name" v-for="option in product.options" :key="option.id">
                                    {{option.name}}
                                </option>
                            </select>
                        </div>
                        <div><strong>{{product.price}} ₽</strong></div>
                        <div>
                            <button class="uk-button-small uk-button uk-button-primary" @click="addItemToCart(product)"
                                    v-if="!checkInCart(product.id)">
                                Купить
                            </button>
                            <div class="uk-inline" v-else>
                                <a class="uk-form-icon" uk-icon="icon: minus"
                                   @click.prevent="decrement(product.id)"></a>
                                <input class="uk-input uk-form-small uk-text-center" readonly
                                       style="padding-right: 40px" type="text" :value="itemCart(product.id).quantity">
                                <a class="uk-form-icon uk-form-icon-flip" uk-icon="icon: plus"
                                   @click.prevent="increment(product.id)"></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapActions, mapGetters } from 'vuex'

    export default {
        name: 'product',
        props: ['product'],
        data: () => ({
            modificator: null
        }),
        mounted () {
            if (this.product.options.length) {
                this.modificator = this.product.options[0].name
            }
        },
        watch: {
            'modificator': function (val) {
                this.product.modifyName = `(${val}) ${this.product.name}`
            }
        },
        computed: {
            ...mapGetters({
                checkInCart: 'cart/checkById',
                itemCart: 'cart/itemById'
            })
        },
        methods: {
            ...mapActions('cart', [
                'addItemToCart',
                'increment',
                'decrement'
            ])
        }
    }
</script>

<style scoped>

</style>