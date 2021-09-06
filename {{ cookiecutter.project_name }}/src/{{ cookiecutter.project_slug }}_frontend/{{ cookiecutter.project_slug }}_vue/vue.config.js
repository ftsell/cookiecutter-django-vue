module.exports = {
    publicPath: "/app",
    integrity: true,
    filenameHashing: false,
    devServer: {
        proxy: {
            "^/api": {
                target: "http://localhost:8000",
            },
        },
    },
};
