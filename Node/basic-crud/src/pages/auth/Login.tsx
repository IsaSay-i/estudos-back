import imgLogin from "../../assets/Login_img.png";

const Login = () => {
  return (
    <div className="flex justify-center items-center bg-grey-fade min-h-screen max-w-full w-screen absolute">
      <section className="flex justify-between bg-white/30 border rounded-xl border-white w-200 py-15 px-20">
        <img src={imgLogin} className="w-43" />
        <form action="POST" className="flex flex-col">
          <h1 className="text-2xl mb-5">Entre com a sua conta</h1>
          <label htmlFor="name" className="font-semibold">Nome</label>
          <input type="text" name="name" id="name" className="mb-3 bg-white/30 w-90 border border-white rounded-md h-8.75 px-2 text-sm" />

          <label htmlFor="email" className="font-semibold">Email</label>
          <input type="email" name="email" id="email" className="mb-3 bg-white/30 w-90 border border-white rounded-md h-8.75 px-2 text-sm" />

          <label htmlFor="pwd" className="font-semibold">Senha</label>
          <input type="password" name="pwd" id="pwd" className="bg-white/30 w-90 border border-white rounded-md h-8.75 px-2 text-sm" />
          <p className="mt-2.75 text-xs flex justify-end">Não tem uma conta?<span><a href="./signUp" className="ml-0.75 underline transition-all duration-300 ease-in-ou hover:font-bold">Cadastre-se aqui</a></span></p>
          <button type="submit" className="w-fit  cursor-pointer mt-auto text-white font-semibold text-shadow-sm border border-white rounded-lg px-6 py-2 bg-[linear-gradient(to_right,_#12FFBC5D_33%,_#1DDAEF5D_100%)]  transition-transform duration-300 hover:bg-[linear-gradient(to_right,_#12FFBC7D_33%,_#1DDAEF7D_100%)] hover:scale-102">Enviar</button>
        </form>
      </section>
    </div>
  );
};

export default Login;
