module.exports = {
    // options...
    runtimeCompiler: true,
    devServer: {
        disableHostCheck: true,
        watchOptions: {
            poll: true
        },
        public: 'http://codeserver:8082'
    },
}
