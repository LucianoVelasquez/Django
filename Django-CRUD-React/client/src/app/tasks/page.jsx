import axios from "axios";
const getTasks = async () => {
  try {
    const res = await axios.get("http://127.0.0.1:3001/tasks/api/v1/tasks/");
    return res.data;
  } catch (error) {
    return console.log(error.message);
  }
};

async function Tasks() {
  const res = await getTasks();

  return (
    <div className="flex flex-col items-center">
      <h1 className="text-5xl m-4">
        Lista de Tasks: 
      </h1>
      <div className="w-60">
        <ul className=" text-left">
          {res == undefined
            ? "No hay Tareas "
            : res.map((e) => {
                return (
                  <>
                    <li className=" hover:bg-slate-900 m-3">
                      {e.id}-{e.title}: {e.description}
                    </li>
                  </>
                );
              })}
        </ul>
      </div>
    </div>
  );
}

export default Tasks;
