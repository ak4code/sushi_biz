const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? ''
        : 'http://localhost:8080/',

    css: {
        extract: true
    },
    filenameHashing: false,
    configureWebpack: {
        plugins: [
            new BundleTracker({ filename: process.env.NODE_ENV === 'production' ? 'webpack-prod-stats.json' : 'webpack-stats.json' })
        ]
    },

    devServer: {
        port: 8080,
        allowedHosts: [
            '127.0.0.1:8000',
            '127.0.0.1'
        ],
        historyApiFallback: true,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
            'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
        }
    },

    runtimeCompiler: true
}
