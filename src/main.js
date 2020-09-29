import Vue from 'vue'
import './plugins/axios'
import store from './store'
import UIkit from 'uikit'
import '@/assets/styles/styles.scss'
import Icons from 'uikit/dist/js/uikit-icons'
import ProductList from '@/components/shop/ProductList'
import Basket from '@/components/shop/Basket'

UIkit.use(Icons)
window.UIkit = UIkit

Vue.config.productionTip = false

new Vue({
    store,
    el: '#ss-biz',
    components: {
        ProductList,
        Basket
    }
})
