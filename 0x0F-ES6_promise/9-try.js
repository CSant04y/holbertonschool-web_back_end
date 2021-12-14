export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const dividend = mathFunction();
    queue.push(dividend);
  } catch (err) {
    queue.push(err.message);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
