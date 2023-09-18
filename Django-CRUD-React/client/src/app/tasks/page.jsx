import axios from "axios";
const getTasks = async () => {
  const res = await axios.get("http://127.0.0.1:3001/tasks/api/v1/tasks/");
  return res.data;
};

async function Tasks() {
  const res = await getTasks();
  console.log(res);
  return (
    <>
      <h1 className="text-5xl m-4 justify-center text-center">
        Lista de Tasks
      </h1>
      <ul className=" text-center">
        {res.map((e) => {
          return(
            <><li>{e.id}-{e.title}: {e.description}</li></>
          )
        })}
      </ul>
    </>
  );
}

export default Tasks;
