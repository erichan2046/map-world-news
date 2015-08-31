module.exports = {
    entry: './web/app.es6',
    output: {
        path: require('path').resolve('./web'),
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.less$/, loader: 'style-loader!css-loader!less-loader' }
        ]
    }
};
