const userController = {
  get: async (req, res) => {
    try {
      const { username } = req.params;
      res.status(200).send({
        user: username
      });
    } catch (err) {
      console.log(err);
      res.status(500).send({
        error: "server error"
      });
    }
  }
};

export default userController;
