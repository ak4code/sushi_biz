<template>
    <div class="ss-product-list uk-margin-top" style="min-height: 600px">
        <div v-if="loading && !page">
            <div class="uk-flex uk-flex-center">
                <div class="uk-height-medium uk-text-center uk-padding-large uk-margin-top">
                    <span uk-spinner="ratio: 4.5"></span>
                    <h4>Загрузка...</h4>
                </div>
            </div>
        </div>
        <div v-else>
            <div v-if="page.count">
                <div class="uk-flex uk-flex-wrap uk-grid-match uk-grid-small uk-child-width-1-5@l uk-child-width-1-4@m uk-child-width-1-3@s uk-child-width-1-2">
                    <div v-for="product in this.page.results" :key="product.id">
                        <product :product="product"></product>
                    </div>
                </div>
                <div class="uk-flex uk-flex-center uk-grid-small">
                    <div v-if="page.next">
                        <a class="uk-button uk-button-primary uk-border-rounded" @click="nextPage(page.next)">
                            Показать еще
                        </a>
                    </div>
                </div>
            </div>
            <div v-else>
                Категория пуста
            </div>
        </div>
    </div>
</template>

<script>
    import Product from './Product';

    export default {
        name: 'product-list',
        props: ['categoryId'],
        data: () => ({
            loading: true,
            innerLoading: false,
            page: null
        }),
        components: {
            Product
        },
        created () {
            this.getProducts(this.categoryId)
        },
        methods: {
            async getProducts (categoryId) {
                let { data } = await this.$axios.get(`/api/categories/${categoryId}/products`)
                this.page = data
                this.loading = false
            },
            async nextPage (url) {
                this.loading = true
                let { data } = await this.$axios.get(url)
                this.page.results.push(...data.results)
                this.page.next = data.next
            }
        }
    }
</script>

<style scoped>

</style>