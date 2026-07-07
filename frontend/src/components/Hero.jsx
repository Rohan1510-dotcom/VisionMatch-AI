function Hero(props) {
  return (
    <section className="hero">

      <h1>{props.heading}</h1>

      <p>{props.description}</p>

    </section>
  );
}

export default Hero;