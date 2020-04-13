module.exports = {
  lintOnSave: false,
  devServer: {
    disableHostCheck: true
  },
  publicPath: process.env.NODE_ENV === 'production'
      ? '/vue/'
      : '/'
};
